---
symbol: "BTNL12P"
type: "gene"
col: 14244
ensembl_id: "ENSG00000240661"
name: "butyrophilin like 12, pseudogene"
location: "3q13.33"
module: 21
arm: "+"
pooled_cpm: 3.43
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# BTNL12P

*butyrophilin like 12, pseudogene* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.16× (z +19.4, q 0e+00, up in 32 of 34 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0743×); [[Vilanterol (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0808×); [[Futibatinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0579×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C12orf40]] (+0.72, fdr 1e-05), [[SGCD]] (+0.71, fdr 7e-06), [[HRG-AS1]] (+0.71, fdr 3e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14244.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.16×** | +19.4 | 0e+00 | 32/34 (HEC-1-A, A498, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.89×** | +16.2 | 0e+00 | 11/16 (HOP62, J82, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.83×** | +11.9 | 2e-30 | 6/8 (A498, J82, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +11.2 | 6e-27 | 6/9 (A-172, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.2 | 3e-14 | 20/37 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~4% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +6.8 | 1e-09 | 9/33 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.76×** | +6.7 | 1e-09 | 8/19 (SW480, PANC-1, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.4 | 1e-08 | 16/41 (HEC-1-A, NCI-H2347, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.33×** | +4.9 | 6e-05 | 5/36 (NCI-H2347, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.3 | 9e-04 | 2/17 (NCI-H2347, C32) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.8 | 0.006 | 3/44 (LS 180, KATO III, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.007 | 6/46 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.8 | 0.008 | 7/46 (HEC-1-A, HOP62, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.34×** | +3.5 | 0.019 | 4/29 (LOX-IMVI, NCI-H460, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.023 | 1/28 (Panc 03.27) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.024 | 1/38 (HEC-1-A) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.046 | 6/45 (NCI-H2347, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.056 | 4/35 (HOP62, A498, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.1 | 0.060 | 6/45 (NCI-H1573, NCI-H661, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +3.0 | 0.063 | 2/41 (NCI-H2347, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +2.9 | 0.079 | 5/45 (CFPAC-1, A-172, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14244.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Raltitrexed (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0743×); [[Vilanterol (drug)]] 0.5 µM in 1 line (LOX-IMVI 0.0808×); [[Futibatinib (drug)]] 0.05 µM in 1 line (SNU-423 0.0579×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.731× | -3.7 | 0.12 | 6/46 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.820× | -3.3 | 0.26 | 3/45 (SNU-423, SW480, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | 0.754× | -3.2 | 0.26 | 6/40 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.925× | -3.0 | 0.34 | 9/47 (SW1417, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14244. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 3.19 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.82× (z +8.7) | [[Raltitrexed (drug)]] 0.5 µM 0.0743× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 2.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 3.36 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0808× (z -8.6) |
| [[SNU-423 (line)]] | alt | 3.44 | 0 | 1 | — | [[Futibatinib (drug)]] 0.05 µM 0.0579× (z -8.5) |
| [[A-172 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.56 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.97 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.20 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14244), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C12orf40]] | +0.72 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[SGCD]] | +0.71 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[HRG-AS1]] | +0.71 | +0.43 / +0.70 | both halves | 3e-05 |  |
| [[CFAP20DC-DT]] | +0.70 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.70 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[LANCL1-AS1]] | +0.70 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[DCC]] | +0.69 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[GEMIN7-AS1]] | +0.68 | +0.44 / +0.67 | both halves | 3e-05 |  |
| [[SLC13A4]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[ABHD15-AS1]] | +0.65 | +0.37 / +0.65 | both halves | 9e-05 |  |
| [[DPYD-AS1]] | +0.65 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[ST8SIA1]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BTNL12P's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.683). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, 23.1); signed map (35.1, 8.9). **Vector** length 42.6, 4.38% of its response variance represented; |z| ≥ 3 in 996 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +19.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.0 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.7 | +16.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.5 | +11.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.5 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.4 | +3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.6 | +0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.3 | +1.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -0.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.2 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -1.7 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin like 12, pseudogene |
| Locus type | pseudogene |
| Location | 3q13.33 — chr3:120,357,754-120,367,874 (+) |
| Ensembl biotype | transcribed_unitary_pseudogene |
| Also known as | ; previously LRRC58-DT |
| Gene groups (HGNC) | Unitary pseudogenes |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:52935](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:52935) · Entrez [100130701](https://www.ncbi.nlm.nih.gov/gene/100130701) · Ensembl [ENSG00000240661](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000240661)

## Data

Gene col 14244: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14244); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14244, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14244]; `tensor/DDL_lfc|DDL_z.npy` [14244]; `embed/gene_vectors.npy` [14244]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14244 or target_col == 14244). Every well: [[BTNL12P — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTNL12P.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
