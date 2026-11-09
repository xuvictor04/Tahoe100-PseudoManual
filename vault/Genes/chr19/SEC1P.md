---
symbol: "SEC1P"
type: "gene"
col: 13871
ensembl_id: "ENSG00000232871"
name: "fucosyltransferase 2B, pseudogene"
location: "19q13.33"
module: 53
arm: "+"
pooled_cpm: 2.12
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# SEC1P

*fucosyltransferase 2B, pseudogene* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.49× (z +20.4, q 0e+00, up in 29 of 29 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0743×; ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0754×; ⚠ cell-cycle shift, explains ~47% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRT3]] (+0.78, fdr 7e-06), [[TMPRSS9]] (+0.76, fdr 7e-06), [[PEBP4]] (+0.74, fdr 7e-06).
> It is in [[Module 053]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13871.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.49×** | +20.4 | 0e+00 | 29/29 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.55×** | +17.2 | 0e+00 | 25/33 (HS-578T, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.42×** | +11.8 | 8e-30 | 8/11 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.49×** | +11.5 | 1e-28 | 1/1 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **3.31×** | +11.5 | 2e-28 | 28/38 (SW480, HEC-1-A, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.43×** | +10.5 | 1e-23 | 2/2 (SW1417, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.47×** | +5.2 | 1e-05 | 7/43 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +5.1 | 2e-05 | 3/5 (NCI-H2347, SW1417, …) | rises with dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 1e-04 | 10/30 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +4.8 | 1e-04 | 7/43 (LoVo, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.57×** | +4.2 | 0.002 | 10/38 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.7 | 0.010 | 8/45 (NCI-H1792, LoVo, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.71×** | +3.7 | 0.010 | 5/42 (NCI-H2347, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +3.7 | 0.010 | 0/4 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.99×** | +3.4 | 0.021 | 1/1 (NCI-H2347) | top dose only | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | **1.45×** | +3.4 | 0.024 | 3/24 (NCI-H2030, HT-29, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.027 | 3/44 (KATO III, H4, …) | rises with dose |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.060 | 2/24 (SW1417, SW480) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Gemfibrozil (drug)]] 0.05 µM |  | **1.37×** | +3.0 | 0.066 | 3/39 (NCI-H1573, SW1417, …) | inconsistent across doses | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.81×** | +3.0 | 0.071 | 0/22 | inconsistent across doses | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +2.9 | 0.098 | 5/26 (HEC-1-A, SW480, …) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13871.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Daptomycin (drug)]] 0.5 µM in 1 line (HEC-1-A 0.0743×; ⚠ unreliable plate only); [[Digitoxin (drug)]] 0.05 µM in 1 line (PANC-1 0.0754×; ⚠ cell-cycle shift, explains ~47% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dimethyl fumarate (drug)]] 0.05 µM |  | 0.660× | -3.5 | 0.22 | 3/38 (C-33 A, LoVo, …) | inconsistent across doses |  |
| [[Bisoprolol (hemifumarate) (drug)]] 0.5 µM |  | 0.726× | -3.1 | 0.43 | 5/39 (LS 180, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.730× | -3.1 | 0.43 | 13/40 (Panc 03.27, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13871. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.73 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.70× (z +9.8) | [[Daptomycin (drug)]] 0.5 µM 0.0743× (z -9.5) ⚠ unreliable plate only |
| [[A-172 (line)]] | wt | 1.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +8.8) | — |
| [[HS-578T (line)]] | alt | 2.16 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 1.15 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0754× (z -8.5) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-427 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.44 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.38 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.26 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.36 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13871), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRT3]] | +0.78 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[TMPRSS9]] | +0.76 | +0.81 / +0.76 | both halves | 7e-06 |  |
| [[PEBP4]] | +0.74 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[DNAH10]] | +0.74 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[SUMO2P17]] | +0.73 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[GRIK5]] | +0.73 | +0.72 / +0.64 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.73 | +0.72 / +0.61 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.72 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[ASB14]] | +0.72 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[DPP6]] | +0.72 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[KCNIP1]] | +0.72 | +0.69 / +0.67 | both halves | 7e-06 |  |
| [[C2CD6]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.805). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (15.5, 24.0); signed map (22.7, 11.9). **Vector** length 48.6, 5.79% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +20.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | +11.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +11.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +17.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.3 | +10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.2 | +3.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.5 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | +2.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.2 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | -0.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.1 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 2B, pseudogene |
| Locus type | pseudogene |
| Location | 19q13.33 — chr19:48,680,081-48,681,020 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | SEC1; previously SEC1P |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [653677](https://www.ncbi.nlm.nih.gov/gene/653677):

> Predicted to enable galactoside 2-alpha-L-fucosyltransferase activity. Predicted to be involved in oligosaccharide biosynthetic process. Predicted to act upstream of or within glycoprotein biosynthetic process. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:44149](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:44149) · Entrez [653677](https://www.ncbi.nlm.nih.gov/gene/653677) · Ensembl [ENSG00000232871](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232871)

## Data

Gene col 13871: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13871); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13871, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13871]; `tensor/DDL_lfc|DDL_z.npy` [13871]; `embed/gene_vectors.npy` [13871]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13871 or target_col == 13871). Every well: [[SEC1P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEC1P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
