---
symbol: "PNPLA3"
type: "gene"
col: 1932
ensembl_id: "ENSG00000100344"
name: "patatin like domain 3, 1-acylglycerol-3-phosphate O-acyltransferase"
location: "22q13.31"
module: 86
arm: "+"
pooled_cpm: 9.94
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 8
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# PNPLA3

*patatin like domain 3, 1-acylglycerol-3-phosphate O-acyltransferase* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.86× (z +13.5, q 6e-39, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.698× (z -5.6, q 2e-05, down in 17 of 46 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDPS]] (+0.69, fdr 7e-06), [[PCSK9]] (+0.67, fdr 1e-05), [[HMGCR]] (+0.67, fdr 7e-06); moves opposite to [[CASC2]] (-0.42, fdr 2e-04), [[STX17]] (-0.38, fdr 9e-04, ⚠ not reproduced), [[USP40]] (-0.35, fdr 0.001, ⚠ one half only (not replicated)), [[NSMCE2]] (-0.35, fdr 6e-04), [[MAP2]] (-0.35, fdr 5e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PMFBP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1932.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +13.5 | 6e-39 | 35/44 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Cepharanthine (drug)]] 5 µM |  | **1.77×** | +12.4 | 7e-33 | 36/46 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Berbamine (drug)]] 5 µM |  | **1.59×** | +10.2 | 6e-22 | 31/46 (NCI-H23, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.68×** | +7.9 | 3e-13 | 22/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.70×** | +7.9 | 4e-13 | 20/41 (NCI-H23, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.51×** | +6.4 | 2e-08 | 22/46 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.09×** | +5.9 | 2e-07 | 16/35 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.30×** | +5.7 | 1e-06 | 16/46 (CFPAC-1, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +5.7 | 1e-06 | 23/45 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +5.4 | 3e-06 | 15/44 (NCI-H460, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.41×** | +5.3 | 7e-06 | 20/46 (HOP62, PANC-1, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.81×** | +4.8 | 8e-05 | 9/46 (HOP62, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | **1.37×** | +4.6 | 2e-04 | 10/46 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.35×** | +4.6 | 2e-04 | 6/46 (NCI-H460, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.23×** | +4.5 | 3e-04 | 17/45 (HOP62, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.3 | 6e-04 | 13/46 (LS 180, C32, …) | top dose only | plate-row cell shift |
| [[Ritonavir (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.001 | 8/45 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +4.0 | 0.002 | 10/46 (COLO 205, HepG2/C3A, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.003 | 16/45 (C32, RPMI-7951, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.56×** | +3.6 | 0.010 | 2/43 (SW480, HS-578T) | top dose only | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.014 | 7/45 (LS 180, COLO 205, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1932.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.698×** | -5.6 | 2e-05 | 17/46 (NCI-H1792, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.752×** | -4.1 | 0.013 | 15/44 (hTERT-HPNE, J82, …) | all doses, flat | low cells (technical?) |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.778×** | -3.9 | 0.020 | 9/45 (HCT15, SW480, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM |  | **0.770×** | -3.8 | 0.023 | 9/46 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.641×** | -3.6 | 0.038 | 9/41 (LS 180, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.798×** | -3.5 | 0.044 | 9/46 (CFPAC-1, PANC-1, …) | rises with dose |  |
| [[Belumosudil (mesylate) (drug)]] 5 µM |  | **0.657×** | -3.4 | 0.057 | 8/43 (NCI-H460, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.806×** | -3.2 | 0.097 | 14/46 (RPMI-7951, NCI-H1792, …) | all doses, flat | composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.810× | -3.1 | 0.11 | 12/44 (COLO 205, NCI-H1792, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 0.870× | -3.1 | 0.12 | 9/46 (Hs 766T, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.822× | -3.0 | 0.12 | 9/45 (NCI-H1792, RPMI-7951, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | 0.689× | -3.0 | 0.12 | 7/20 (SW480, NCI-H460, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1932. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 17.4 | 2 | 1 | [[Cepharanthine (drug)]] 5 µM 3.69× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -9.8) ⚠ toxic · without an alert: [[Pralsetinib (drug)]] 5 µM 0.0419× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.74 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.16× (z +12.8) | [[Docetaxel (drug)]] 0.05 µM 0.0977× (z -12.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 8.19 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +9.6) | — |
| [[A549 (line)]] | wt | 4.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +8.8) | — |
| [[LS 180 (line)]] | wt | 9.22 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 3.83× (z +8.9) | — |
| [[RPMI-7951 (line)]] | alt | 28.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 16.3 | 0 | 1 | — | [[Talc (drug)]] 0.05 µM 0.123× (z -9.0) |
| [[SW480 (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.90 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.47 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.58 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.16 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.13 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.44 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.60 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1932), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDPS]] | +0.69 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[PCSK9]] | +0.67 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[HMGCR]] | +0.67 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[MSMO1]] | +0.66 | +0.60 / +0.68 | both halves | 7e-06 |  |
| [[ACSS2]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[FDFT1]] | +0.65 | +0.65 / +0.67 | both halves | 7e-06 | STRING 632 |
| [[ACAT2]] | +0.61 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SCD]] | +0.61 | +0.60 / +0.51 | both halves | 1e-05 | STRING 515 |
| [[DHCR7]] | +0.61 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[MVD]] | +0.59 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[FASN]] | +0.59 | +0.61 / +0.49 | both halves | 1e-05 | same gene group; STRING 656 |
| [[HMGCS1]] | +0.58 | +0.63 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 6 of them with an alert (⚠; 6 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASC2]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[STX17]] | -0.38 | -0.18 / -0.48 | ⚠ not reproduced | 9e-04 |  |
| [[USP40]] | -0.35 | -0.17 / -0.54 | ⚠ one half (not replicated) | 0.001 |  |
| [[NSMCE2]] | -0.35 | -0.22 / -0.43 | both halves | 6e-04 |  |
| [[PMFBP1]] | -0.35 | -0.14 / -0.41 | ⚠ not reproduced | 0.002 |  |
| [[SLC38A4-AS1]] | -0.35 | -0.19 / -0.53 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MAP2]] | -0.35 | -0.24 / -0.28 | both halves | 5e-04 |  |
| [[ATF6]] | -0.34 | -0.18 / -0.36 | ⚠ not reproduced | 1e-03 |  |
| [[ID4]] | -0.34 | -0.19 / -0.26 | ⚠ not reproduced | 8e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMFBP1]] | B | PMFBP1 activity raises PNPLA3's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.91× lower at baseline in the lines without PMFBP1 | 0.098 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.686). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.4, -49.4); signed map (-52.8, 32.7). **Vector** length 74.8, 12.6% of its response variance represented; |z| ≥ 3 in 973 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.56 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.55 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.55 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.3 | +13.5 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +4.5 | +12.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.7 | +7.9 |
|  | [[Berbamine (drug)]] 5 µM |  | +3.6 | +10.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.0 | -0.7 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +5.7 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +4.3 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.5 | -5.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.2 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.8 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | patatin like domain 3, 1-acylglycerol-3-phosphate O-acyltransferase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:43,923,792-43,964,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ796I17.1, FLJ22012, adiponutrin, iPLA2epsilon; previously C22orf20, ADPN |
| Gene groups (HGNC) | Lipases; Patatin like phospholipase domain containing; Acyltransferases |
| Reactome | 4 pathways, smallest: Acyl chain remodeling of DAG and TAG; Glycerophospholipid biosynthesis; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NST1](https://www.uniprot.org/uniprotkb/Q9NST1) (1-acylglycerol-3-phosphate O-acyltransferase PNPLA3):

> Specifically catalyzes coenzyme A (CoA)-dependent acylation of 1-acyl-sn-glycerol 3-phosphate (2-lysophosphatidic acid/LPA) to generate phosphatidic acid (PA), an important metabolic intermediate and precursor for both triglycerides and glycerophospholipids. Does not esterify other lysophospholipids. Acyl donors are long chain (at least C16) fatty acyl-CoAs: arachidonoyl-CoA, linoleoyl-CoA, oleoyl-CoA and at a lesser extent palmitoyl-CoA. Additionally possesses low triacylglycerol lipase and …

**Summary**, from NCBI Gene [80339](https://www.ncbi.nlm.nih.gov/gene/80339):

> The protein encoded by this gene is a triacylglycerol lipase that mediates triacylglycerol hydrolysis in adipocytes. The encoded protein, which appears to be membrane bound, may be involved in the balance of energy usage/storage in adipocytes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18590](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18590) · Entrez [80339](https://www.ncbi.nlm.nih.gov/gene/80339) · UniProt [Q9NST1](https://www.uniprot.org/uniprotkb/Q9NST1) · Ensembl [ENSG00000100344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100344)

## Data

Gene col 1932: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1932); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1932, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1932]; `tensor/DDL_lfc|DDL_z.npy` [1932]; `embed/gene_vectors.npy` [1932]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1932 or target_col == 1932). Every well: [[PNPLA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNPLA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
