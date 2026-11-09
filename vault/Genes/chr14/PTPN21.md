---
symbol: "PTPN21"
type: "gene"
col: 966
ensembl_id: "ENSG00000070778"
name: "protein tyrosine phosphatase non-receptor type 21"
location: "14q31.3"
module: 79
arm: "+"
pooled_cpm: 25.31
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 9
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# PTPN21

*protein tyrosine phosphatase non-receptor type 21* — 14q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.69× (z +8.2, q 2e-13, up in 34 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.44× (z +8.0, q 5e-13, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.625× (z -10.5, q 6e-23, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ACOT9]] (+0.75, fdr 7e-06), [[TNFRSF12A]] (+0.64, fdr 7e-06), [[PSEN2]] (+0.64, fdr 7e-06); moves opposite to [[SPICE1]] (-0.66, fdr 7e-06), [[GGA2]] (-0.60, fdr 1e-05), [[SNHG30]] (-0.59, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 966.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.69×** | +8.2 | 2e-13 | 34/47 (NCI-H1573, BT-474, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +8.0 | 5e-13 | 28/47 (NCI-H23, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **1.70×** | +7.8 | 9e-13 | 34/47 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.64×** | +7.7 | 2e-12 | 25/47 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +5.8 | 9e-07 | 22/47 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.43×** | +5.6 | 3e-06 | 27/47 (NCI-H1573, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +5.4 | 6e-06 | 26/48 (NCI-H1573, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 24/47 (A-427, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.39×** | +5.1 | 2e-05 | 20/47 (C-33 A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.38×** | +5.0 | 3e-05 | 24/47 (NCI-H1573, C-33 A, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.37×** | +4.8 | 6e-05 | 20/47 (LS 180, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +4.3 | 7e-04 | 18/47 (A-172, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.2 | 0.001 | 19/48 (C-33 A, SNU-1, …) | all doses, stronger at high dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.32×** | +4.0 | 0.002 | 14/46 (NCI-H2030, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.20× | +3.9 | 0.003 | 14/48 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +3.8 | 0.006 | 18/48 (NCI-H2030, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 6 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 966.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.625×** | -10.5 | 6e-23 | 34/47 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.686×** | -6.0 | 8e-07 | 26/47 (SW480, SNU-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.732×** | -4.6 | 5e-04 | 22/46 (HEC-1-A, RKO, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.746×** | -4.6 | 5e-04 | 22/48 (LOX-IMVI, SW480, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -4.6 | 5e-04 | 20/47 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.753×** | -4.5 | 7e-04 | 20/47 (LOX-IMVI, SW480, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.764×** | -4.3 | 0.002 | 21/46 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.756×** | -4.2 | 0.002 | 22/47 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.794×** | -3.7 | 0.016 | 18/48 (LOX-IMVI, SW480, …) | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 966. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 59.1 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -16.0) |
| [[HEC-1-A (line)]] | alt | 46.6 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.254× (z -12.8) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.479× (z -10.4) |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -13.7) |
| [[A-427 (line)]] | wt | 46.5 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.71× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.139× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 37.6 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.178× (z -11.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.292× (z -9.0) |
| [[COLO 205 (line)]] | alt | 7.95 | 0 | 2 | — | [[Procainamide (hydrochloride) (drug)]] 5 µM 0.0788× (z -8.6) |
| [[KATO III (line)]] | alt | 21.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.207× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.246× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 44.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.352× (z -11.5) |
| [[NCI-H23 (line)]] | alt | 15.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.01× (z +10.8) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.117× (z -11.1) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SNU-1 (line)]] | wt | 30.8 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0792× (z -13.3) |
| [[SW480 (line)]] | alt | 34.0 | 0 | 2 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.265× (z -14.3) |
| [[A549 (line)]] | wt | 43.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.488× (z -8.5) |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.140× (z -10.2) |
| [[HCT15 (line)]] | alt | 21.5 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.101× (z -11.3) |
| [[HS-578T (line)]] | alt | 19.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 1 | — | [[Simotinib (drug)]] 0.05 µM 0.0753× (z -11.0) |
| [[PANC-1 (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.256× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A-172 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 966), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*61 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACOT9]] | +0.75 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[TNFRSF12A]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[PSEN2]] | +0.64 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[RASAL2]] | +0.60 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[SRGAP1]] | +0.59 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SNX24]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TXNRD3]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[CPLANE1]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ABL2]] | +0.56 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[EIF3J]] | +0.56 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CDV3]] | +0.55 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[SHTN1]] | +0.55 | +0.50 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*39 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPICE1]] | -0.66 | -0.62 / -0.64 | both halves | 7e-06 |  |
| [[GGA2]] | -0.60 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.59 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PIK3C2A]] | -0.57 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[PDK3]] | -0.57 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[FAM13A]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SRP54-AS1]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[ALKBH5]] | -0.56 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[RNASET2]] | -0.55 | -0.37 / -0.59 | both halves | 9e-05 |  |
| [[BMT2]] | -0.54 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[RAB20]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity lowers PTPN21's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 1.76× higher at baseline in the lines without RAB20 | 0.036 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises PTPN21's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises PTPN21's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction -0.483). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (7.8, -19.0); signed map (10.7, 40.5). **Vector** length 104, 24.6% of its response variance represented; |z| ≥ 3 in 1,002 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.6 | +7.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +6.1 | +7.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +6.0 | +5.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.3 | +5.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +5.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +4.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +4.6 | +5.0 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.4 | -10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.2 | -6.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.9 | -4.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.6 | -2.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -4.6 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Allopurinol (drug)]] 0.05 µM |  | -1.5 | -1.3 |
|  | [[Pimitespib (drug)]] 0.05 µM |  | -1.5 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 21 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q31.3 — chr14:88,465,778-88,555,007 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PTPD1, PTPRL10 |
| Gene groups (HGNC) | Protein tyrosine phosphatases non-receptor type; FERM domain containing |
| Hallmark sets | ANDROGEN_RESPONSE, UV_RESPONSE_DN |
| Matched by | ensembl_id |

UniProt [Q16825](https://www.uniprot.org/uniprotkb/Q16825) carries no function annotation.

**Summary**, from NCBI Gene [11099](https://www.ncbi.nlm.nih.gov/gene/11099):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. This PTP contains an N-terminal domain, similar to cytoskeletal- associated proteins including band 4.1, ezrin, merlin, and radixin. This PTP was shown to specially interact with BMX/ETK, a member of Tec tyrosine kinase family …

**Accessions** — [HGNC:9651](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9651) · Entrez [11099](https://www.ncbi.nlm.nih.gov/gene/11099) · UniProt [Q16825](https://www.uniprot.org/uniprotkb/Q16825) · Ensembl [ENSG00000070778](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000070778)

## Data

Gene col 966: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 966); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 966, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 966]; `tensor/DDL_lfc|DDL_z.npy` [966]; `embed/gene_vectors.npy` [966]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 966 or target_col == 966). Every well: [[PTPN21 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN21.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
