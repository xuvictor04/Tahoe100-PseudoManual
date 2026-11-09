---
symbol: "MAP2K2"
type: "gene"
col: 4779
ensembl_id: "ENSG00000126934"
name: "mitogen-activated protein kinase kinase 2"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 27.04
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 2
n_dd_up_clean: 11
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 150
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# MAP2K2

*mitogen-activated protein kinase kinase 2* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.74× (z +7.8, q 4e-12, up in 34 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.51× (z +5.8, q 1e-06, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Selinexor (drug)]] 5 µM: 0.766× (z -5.0, q 3e-04, down in 25 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.241×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.186×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Folic acid (drug)]] 5 µM in 1 line (Hs 766T 0.335×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM259]] (+0.74, fdr 7e-06), [[GOLGA6L9]] (+0.71, fdr 7e-06), [[DDRGK1]] (+0.65, fdr 7e-06); moves opposite to [[TFAM]] (-0.59, fdr 1e-05), [[DR1]] (-0.55, fdr 1e-05), [[EIF4G2]] (-0.54, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 150 go from it, the strongest it → [[ACP7]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +7.8 | 4e-12 | 34/44 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +7.4 | 4e-11 | 25/35 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.51×** | +5.8 | 1e-06 | 34/48 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.48×** | +5.2 | 4e-05 | 31/48 (A498, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.7 | 3e-04 | 27/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 9e-04 | 26/48 (C32, HOP62, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.3 | 0.001 | 25/46 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.1 | 0.003 | 21/45 (AN3 CA, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.37×** | +4.1 | 0.003 | 19/41 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.58×** | +3.9 | 0.007 | 23/48 (J82, HOP62, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.57×** | +3.8 | 0.007 | 25/46 (PANC-1, LS 180, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.50×** | +3.4 | 0.029 | 13/48 (NCI-H460, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.4 | 0.029 | 19/48 (AsPC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.49×** | +3.4 | 0.029 | 15/45 (NCI-H460, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.27×** | +3.3 | 0.035 | 20/48 (SW1417, NCI-H1792, …) | rises with dose | composition shift |
| [[vincristine (drug)]] 0.5 µM |  | **1.45×** | +3.2 | 0.055 | 8/48 (NCI-H460, HOP62, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.072 | 13/47 (PANC-1, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4779.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (HT-29 0.241×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (SHP-77 0.186×; ⚠ toxic; transcription drop); [[Doxorubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Folic acid (drug)]] 5 µM in 1 line (Hs 766T 0.335×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.766×** | -5.0 | 3e-04 | 25/48 (SW 900, PANC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.754×** | -3.7 | 0.065 | 18/48 (A-172, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.788× | -3.1 | 0.24 | 15/48 (NCI-H2347, A549, …) | inconsistent across doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.768× | -3.1 | 0.24 | 12/48 (LoVo, HT-29, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Pexidartinib (hydrochloride) (drug)]] 0.05 µM |  | 0.790× | -3.1 | 0.24 | 10/47 (HT-29, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 22.2 | 0 | 1 | — | [[Folic acid (drug)]] 5 µM 0.335× (z -8.9) |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 18.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.86× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 29.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 33.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.9) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 43.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.304× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 19.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -9.9) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 37.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM259]] | +0.74 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[GOLGA6L9]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[DDRGK1]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[TOM1]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[FHIP2B]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[FXR2]] | +0.59 | +0.43 / +0.61 | both halves | 3e-05 |  |
| [[EGFL8]] | +0.59 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[SAMD4B]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[GDPD3]] | +0.57 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[SDHAP1-1]] | +0.57 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[EDF1]] | +0.57 | +0.46 / +0.57 | both halves | 3e-05 |  |
| [[GDI1]] | +0.56 | +0.57 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TFAM]] | -0.59 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[DR1]] | -0.55 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[EIF4G2]] | -0.54 | -0.45 / -0.64 | both halves | 3e-05 |  |
| [[SMIM15]] | -0.53 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[AKAP11]] | -0.52 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[ALG10]] | -0.52 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[ZNF816]] | -0.51 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[CHRAC1]] | -0.51 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[C9orf64]] | -0.51 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[TWF1]] | -0.51 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[FH]] | -0.51 | -0.55 / -0.38 | both halves | 6e-05 |  |
| [[ADAT1]] | -0.50 | -0.45 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*150 arrows, 150 of them with an alert ⚠; grade A 0, B 150, C 0. Shown: the 12 strongest; 138 more arrows (138 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACP7]] | B | MAP2K2 activity raises ACP7's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets |
| [[DCLK2]] | B | MAP2K2 activity lowers DCLK2's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ENSG00000287929]] | B | MAP2K2 activity raises ENSG00000287929's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[ARC]] | B | MAP2K2 activity raises ARC's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CCT2]] | B | MAP2K2 activity raises CCT2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[EPHA2-AS1]] | B | MAP2K2 activity raises EPHA2-AS1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LINC00963]] | B | MAP2K2 activity lowers LINC00963's level | compounds that target MAP2K2: 2 of 2 raise it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[LINC01589]] | B | MAP2K2 activity raises LINC01589's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[LRFN5]] | B | MAP2K2 activity raises LRFN5's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[PFDN2]] | B | MAP2K2 activity raises PFDN2's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets |
| [[PRKG2-AS1]] | B | MAP2K2 activity raises PRKG2-AS1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[RRP9]] | B | MAP2K2 activity raises RRP9's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-4.0, -19.3); signed map (-28.1, 2.0). **Vector** length 78.6, 17.7% of its response variance represented; |z| ≥ 3 in 576 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +4.7 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.6 | +5.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +3.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +4.4 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.6 | +3.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +1.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.2 | +2.2 |
| fall | [[Selinexor (drug)]] 5 µM |  | -4.0 | -5.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -1.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -1.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -1.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.9 | -2.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.7 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:4,090,321-4,124,122 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MEK2, MKK2; previously PRKMK2 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinases |
| Reactome | 32 pathways, smallest: Signaling by MAP2K mutants; Negative feedback regulation of MAPK pathway; MAPK1 (ERK2) activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P36507](https://www.uniprot.org/uniprotkb/P36507) (Dual specificity mitogen-activated protein kinase kinase 2):

> Catalyzes the concomitant phosphorylation of a threonine and a tyrosine residue in a Thr-Glu-Tyr sequence located in MAP kinases. Activates the ERK1 and ERK2 MAP kinases (By similarity). Activates BRAF in a KSR1 or KSR2-dependent manner; by binding to KSR1 or KSR2 releases the inhibitory intramolecular interaction between KSR1 or KSR2 protein kinase and N-terminal domains which promotes KSR1 or KSR2-BRAF dimerization and BRAF activation.

**Summary**, from NCBI Gene [5605](https://www.ncbi.nlm.nih.gov/gene/5605):

> The protein encoded by this gene is a dual specificity protein kinase that belongs to the MAP kinase kinase family. This kinase is known to play a critical role in mitogen growth factor signal transduction. It phosphorylates and thus activates MAPK1/ERK2 and MAPK2/ERK3. The activation of this kinase itself is dependent on the Ser/Thr phosphorylation by MAP kinase kinase kinases. Mutations in this gene cause cardiofaciocutaneous syndrome (CFC syndrome), a disease characterized by heart defects, …

**Accessions** — [HGNC:6842](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6842) · Entrez [5605](https://www.ncbi.nlm.nih.gov/gene/5605) · UniProt [P36507](https://www.uniprot.org/uniprotkb/P36507) · Ensembl [ENSG00000126934](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126934)

## Data

Gene col 4779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4779); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4779]; `tensor/DDL_lfc|DDL_z.npy` [4779]; `embed/gene_vectors.npy` [4779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4779 or target_col == 4779). Every well: [[MAP2K2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP2K2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
