---
symbol: "ASB14"
type: "gene"
col: 14192
ensembl_id: "ENSG00000239388"
name: "ankyrin repeat and SOCS box containing 14"
location: "3p14.3"
module: 21
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# ASB14

*ankyrin repeat and SOCS box containing 14* — 3p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.93× (z +14.2, q 9e-43, up in 23 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPATC1]] (+0.84, fdr 7e-06), [[EAF1-AS1]] (+0.84, fdr 7e-06), [[PKD2L2]] (+0.81, fdr 7e-06); moves opposite to [[RPE]] (-0.64, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14192.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.93×** | +14.2 | 9e-43 | 23/34 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.07×** | +9.6 | 3e-19 | 23/33 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +8.8 | 3e-16 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +8.3 | 2e-14 | 9/10 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.55×** | +7.5 | 6e-12 | 2/3 (NCI-H2347, A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +5.5 | 4e-06 | 2/9 (HT-29, HEC-1-A) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.73×** | +5.1 | 3e-05 | 16/34 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +4.1 | 0.003 | 6/33 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.007 | 4/27 (PANC-1, LS 180, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.049 | 4/27 (J82, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.95×** | +3.3 | 0.055 | 0/3 | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14192.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.886× | -3.9 | 0.062 | 17/47 (BT-474, NCI-H2347, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.785× | -3.2 | 0.45 | 7/45 (NCI-H1573, J82, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14192. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 3.17 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.65× (z +8.9) | — |
| [[LoVo (line)]] | wt | 2.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 2.00 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.72× (z +8.6) | — |
| [[NCI-H460 (line)]] | wt | 2.10 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.41× (z +8.6) | — |
| [[PANC-1 (line)]] | alt | 1.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.07× (z +9.6) | — |
| [[A-172 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.48 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.56 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14192), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPATC1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[EAF1-AS1]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 |  |
| [[PKD2L2]] | +0.81 | +0.75 / +0.86 | both halves | 7e-06 |  |
| [[CTDSPL2-DT]] | +0.81 | +0.79 / +0.85 | both halves | 7e-06 |  |
| [[TTC36-AS1]] | +0.81 | +0.79 / +0.80 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.81 | +0.82 / +0.78 | both halves | 7e-06 |  |
| [[SPATA21]] | +0.79 | +0.75 / +0.77 | both halves | 7e-06 |  |
| [[TTN]] | +0.79 | +0.84 / +0.68 | both halves | 7e-06 |  |
| [[USH2A]] | +0.78 | +0.78 / +0.76 | both halves | 7e-06 |  |
| [[CHMP3-AS1]] | +0.78 | +0.68 / +0.85 | both halves | 7e-06 |  |
| [[MEIOC]] | +0.77 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[SYNM-AS1]] | +0.77 | +0.80 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPE]] | -0.64 | -0.56 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ASB14's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.764). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 26.7); signed map (32.1, 5.7). **Vector** length 38.4, 3.67% of its response variance represented; |z| ≥ 3 in 985 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.4 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.1 | +5.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.8 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.2 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.4 | -0.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.3 | -0.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -0.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.1 | -3.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -0.9 | -1.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | +0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | ankyrin repeat and SOCS box containing 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p14.3 — chr3:57,268,342-57,292,685 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp313L0121 |
| Gene groups (HGNC) | Ankyrin repeat domain containing |
| Reactome | 4 pathways, smallest: Neddylation; Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NK59](https://www.uniprot.org/uniprotkb/A6NK59) (Ankyrin repeat and SOCS box protein 14):

> May be a substrate-recognition component of a SCF-like ECS (Elongin-Cullin-SOCS-box protein) E3 ubiquitin-protein ligase complex which mediates the ubiquitination and subsequent proteasomal degradation of target proteins. Plays a role in the inhibition of cardiomyocyte nuclear proliferation by mediating the ubiquitination and degradation of MAPRE2.

**Summary**, from NCBI Gene [142686](https://www.ncbi.nlm.nih.gov/gene/142686):

> The protein encoded by this gene is a member of the ankyrin repeat and SOCS box-containing (ASB) family of proteins. They contain ankyrin repeat sequence and a SOCS box domain. The SOCS box serves to couple suppressor of cytokine signalling (SOCS) proteins and their binding partners with the elongin B and C complex, possibly targeting them for degradation. Alternative splicing results in multiple transcript variants encoding different isoforms.[provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:19766](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19766) · Entrez [142686](https://www.ncbi.nlm.nih.gov/gene/142686) · UniProt [A6NK59](https://www.uniprot.org/uniprotkb/A6NK59) · Ensembl [ENSG00000239388](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239388)

## Data

Gene col 14192: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14192); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14192, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14192]; `tensor/DDL_lfc|DDL_z.npy` [14192]; `embed/gene_vectors.npy` [14192]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14192 or target_col == 14192). Every well: [[ASB14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ASB14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
