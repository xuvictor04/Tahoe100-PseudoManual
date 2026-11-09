---
symbol: "LMO7-AS1"
type: "gene"
col: 15325
ensembl_id: "ENSG00000261105"
name: "LMO7 antisense RNA 1"
location: "13q22.2"
module: 10
arm: "+"
pooled_cpm: 3.11
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# LMO7-AS1

*LMO7 antisense RNA 1* — 13q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.35× (z +11.5, q 1e-27, up in 3 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.14× (z +10.6, q 5e-24, up in 18 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.609× (z -4.9, q 5e-04, down in 11 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.301×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.206×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.225×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC8C-DT]] (+0.67, fdr 7e-06), [[ZFP2]] (+0.64, fdr 1e-05), [[SLC13A4]] (+0.63, fdr 1e-05); moves opposite to [[ECHS1]] (-0.53, fdr 1e-04), [[PDHA1]] (-0.53, fdr 7e-05).
> It sits in the **+** arm of [[Module 010]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.35×** | +11.5 | 1e-27 | 3/5 (HS-578T, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.14×** | +10.6 | 5e-24 | 18/28 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +8.6 | 2e-15 | 8/13 (SW480, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.49×** | +7.9 | 6e-13 | 3/5 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.0 | 2e-07 | 10/25 (A498, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.81×** | +5.9 | 4e-07 | 3/12 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.80×** | +5.8 | 5e-07 | 14/34 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.7 | 1e-06 | 16/41 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.2 | 0.001 | 8/32 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +3.5 | 0.025 | 1/29 (C32) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.5 | 0.025 | 3/20 (A-427, NCI-H1792, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.42×** | +3.5 | 0.025 | 2/23 (PANC-1, HOP62) | two highest doses | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.032 | 2/33 (HEC-1-A, HS-578T) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.040 | 4/44 (A-172, SW480, …) | rises with dose |  |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.39×** | +3.3 | 0.040 | 4/39 (PANC-1, A-172, …) | inconsistent across doses | position effect removed |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.090 | 2/25 (NCI-H2030, RKO) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 1 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (PANC-1 0.301×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (PANC-1 0.206×); [[Digitoxin (drug)]] 0.5 µM in 1 line (PANC-1 0.225×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.609×** | -4.9 | 5e-04 | 11/36 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -3.9 | 0.023 | 11/40 (PANC-1, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.697×** | -3.5 | 0.075 | 12/45 (J82, PANC-1, …) | inconsistent across doses |  |
| [[Dimethyl fumarate (drug)]] 5 µM |  | 0.722× | -3.1 | 0.26 | 7/43 (LoVo, H4, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 8.83 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.8) |
| [[Panc 03.27 (line)]] | alt | 3.91 | 0 | 1 | — | [[Neratinib (drug)]] 0.05 µM 0.0685× (z -8.9) |
| [[SW480 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +8.7) | — |
| [[A-172 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.913 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.93 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.59 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.879 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.11 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.10 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.14 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC8C-DT]] | +0.67 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[ZFP2]] | +0.64 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[SLC13A4]] | +0.63 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[ADAP2]] | +0.61 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[LINC02951]] | +0.60 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[ANKRD20A21P]] | +0.60 | +0.63 / +0.40 | both halves | 5e-05 |  |
| [[NSMCE1-DT]] | +0.60 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[GCC2-AS1]] | +0.59 | +0.61 / +0.48 | both halves | 2e-05 | same gene group |
| [[TP53TG5]] | +0.59 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[UPP2]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[ZNF236-DT]] | +0.58 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[BMAL2-AS1]] | +0.58 | +0.46 / +0.60 | both halves | 3e-05 | same gene group |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHS1]] | -0.53 | -0.34 / -0.58 | both halves | 1e-04 |  |
| [[PDHA1]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.415). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (8.8, 30.7); signed map (35.7, -8.5). **Vector** length 39.7, 4.30% of its response variance represented; |z| ≥ 3 in 900 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +5.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.4 | +10.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.2 | +7.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.2 | +1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.2 | +2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.4 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -1.1 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -1.2 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.0 | -2.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -1.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -0.9 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | LMO7 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 13q22.2 — chr13:75,604,700-75,635,994 (-) |
| Ensembl biotype | lncRNA |
| Also known as | UCHL3-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:50277](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50277) · Entrez [101927155](https://www.ncbi.nlm.nih.gov/gene/101927155) · Ensembl [ENSG00000261105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261105)

## Data

Gene col 15325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15325); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15325]; `tensor/DDL_lfc|DDL_z.npy` [15325]; `embed/gene_vectors.npy` [15325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15325 or target_col == 15325). Every well: [[LMO7-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LMO7-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
