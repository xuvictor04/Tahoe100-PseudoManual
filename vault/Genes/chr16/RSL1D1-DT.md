---
symbol: "RSL1D1-DT"
type: "gene"
col: 15410
ensembl_id: "ENSG00000263307"
name: "RSL1D1 divergent transcript"
location: "16p13.13"
module: 21
arm: "+"
pooled_cpm: 25.17
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# RSL1D1-DT

*RSL1D1 divergent transcript* — 16p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.87× (z +15.4, q 0e+00, up in 42 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.262×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (CHP-212 0.0835×; ⚠ cell-cycle shift, explains ~3% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD42-DT]] (+0.69, fdr 3e-05), [[PCF11-AS1]] (+0.67, fdr 8e-06), [[EOGT-DT]] (+0.67, fdr 7e-06); moves opposite to [[NSMCE4A]] (-0.69, fdr 9e-06), [[NIN]] (-0.66, fdr 1e-05), [[PSMG1]] (-0.62, fdr 1e-05).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15410.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +15.4 | 0e+00 | 42/48 (HS-578T, J82, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.64×** | +12.3 | 2e-32 | 40/48 (Hs 766T, J82, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +12.0 | 4e-31 | 44/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +10.7 | 1e-24 | 41/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.80×** | +10.3 | 8e-23 | 39/48 (SW480, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +9.8 | 7e-21 | 36/48 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.75×** | +9.8 | 8e-21 | 42/48 (AsPC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +9.5 | 1e-19 | 29/47 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +8.2 | 2e-14 | 31/45 (NCI-H1573, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.52×** | +7.3 | 1e-11 | 30/48 (Hs 766T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.51×** | +7.2 | 2e-11 | 28/48 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.37×** | +5.3 | 5e-06 | 18/34 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 9e-06 | 24/48 (A-172, HOP62, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.65×** | +4.6 | 2e-04 | 21/48 (A498, KATO III, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.9 | 0.003 | 12/48 (KATO III, A498, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.8 | 0.006 | 19/48 (SW480, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM |  | **1.23×** | +3.6 | 0.011 | 15/48 (HT-29, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15410.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.247×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1573 0.262×; ⚠ toxic; transcription drop); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (CHP-212 0.0835×; ⚠ cell-cycle shift, explains ~3% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Larotrectinib (drug)]] 5 µM |  | 0.868× | -3.5 | 0.25 | 9/48 (H4, PANC-1, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | 0.827× | -3.3 | 0.25 | 17/48 (LoVo, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.882× | -3.1 | 0.34 | 13/48 (NCI-H1792, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15410. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.4 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.49× (z +13.0) | — |
| [[NCI-H460 (line)]] | wt | 20.9 | 4 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +9.7) | — |
| [[A-172 (line)]] | wt | 26.4 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.0) | — |
| [[A498 (line)]] | wt | 27.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[AsPC-1 (line)]] | alt | 34.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.68× (z +10.1) | — |
| [[HOP62 (line)]] | alt | 19.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 19.5 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.60× (z +11.6) | — |
| [[J82 (line)]] | alt | 21.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.0) | — |
| [[NCI-H1573 (line)]] | alt | 34.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.14× (z +8.6) ⚠ toxic | [[Dinaciclib (drug)]] 5 µM 0.262× (z -10.0) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 29.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.89× (z +11.5) | — |
| [[A549 (line)]] | wt | 20.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +8.5) | — |
| [[CFPAC-1 (line)]] | alt | 21.4 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.31× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0835× (z -9.8) ⚠ cell-cycle shift, explains ~3% of this change |
| [[HCT15 (line)]] | alt | 30.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.14× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 26.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +10.3) | — |
| [[Hs 766T (line)]] | wt | 31.5 | 1 | 0 | [[Selinexor (drug)]] 5 µM 2.29× (z +9.0) | — |
| [[LOX-IMVI (line)]] | wt | 17.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 31.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.80× (z +8.5) | — |
| [[RPMI-7951 (line)]] | alt | 38.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.247× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~2% of this change |
| [[SHP-77 (line)]] | alt | 27.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +10.6) | — |
| [[A-427 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15410), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD42-DT]] | +0.69 | +0.43 / +0.66 | both halves | 3e-05 | same gene group |
| [[PCF11-AS1]] | +0.67 | +0.59 / +0.58 | both halves | 8e-06 |  |
| [[EOGT-DT]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | same gene group |
| [[ILF3-DT]] | +0.67 | +0.53 / +0.64 | both halves | 1e-05 | same gene group |
| [[TICAM2-AS1]] | +0.66 | +0.67 / +0.56 | both halves | 1e-05 |  |
| [[SMIM4]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[ZNF490]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[ZRANB2-AS1]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[C12orf73]] | +0.63 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ADNP-AS1]] | +0.62 | +0.63 / +0.47 | both halves | 2e-05 |  |
| [[ZNF814]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NSMCE4A]] | -0.69 | -0.57 / -0.59 | both halves | 9e-06 |  |
| [[NIN]] | -0.66 | -0.61 / -0.52 | both halves | 1e-05 |  |
| [[PSMG1]] | -0.62 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[SSX2IP]] | -0.59 | -0.61 / -0.43 | both halves | 3e-05 |  |
| [[CCT5]] | -0.58 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[VANGL1]] | -0.57 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[ELAC2]] | -0.57 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[SACS]] | -0.57 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[BLMH]] | -0.56 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[PRPS1]] | -0.56 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[TRIM68]] | -0.54 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[RUVBL1]] | -0.54 | -0.43 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RSL1D1-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.618). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-11.2, 24.1); signed map (-1.8, -0.9). **Vector** length 82.4, 16.5% of its response variance represented; |z| ≥ 3 in 1,013 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +5.9 | +12.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +4.6 | +7.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +4.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +15.4 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +3.5 | +3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +2.8 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +3.8 |
|  | [[Bimiralisib (drug)]] 0.05 µM |  | +2.1 | +2.2 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -4.0 | -0.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.3 | +1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -2.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.0 | +2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.7 |
|  | [[Larotrectinib (drug)]] 5 µM |  | -1.7 | -3.5 |
|  | [[Doxycycline (monohydrate) (drug)]] 5 µM |  | -1.6 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | RSL1D1 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 16p13.13 — chr16:11,851,622-11,907,054 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55337) · Entrez [105371084](https://www.ncbi.nlm.nih.gov/gene/105371084) · Ensembl [ENSG00000263307](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000263307)

## Data

Gene col 15410: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15410); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15410, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15410]; `tensor/DDL_lfc|DDL_z.npy` [15410]; `embed/gene_vectors.npy` [15410]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15410 or target_col == 15410). Every well: [[RSL1D1-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RSL1D1-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
