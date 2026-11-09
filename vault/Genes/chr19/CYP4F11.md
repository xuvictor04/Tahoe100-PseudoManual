---
symbol: "CYP4F11"
type: "gene"
col: 10183
ensembl_id: "ENSG00000171903"
name: "cytochrome P450 family 4 subfamily F member 11"
location: "19p13.12"
module: 117
arm: "+"
pooled_cpm: 9.26
n_lines_expressing: 21
n_dd_up: 26
n_dd_down: 5
n_dd_up_clean: 17
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 11
direction_downstream: 24
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# CYP4F11

*cytochrome P450 family 4 subfamily F member 11* — 19p13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 4.57× (z +14.5, q 6e-45, up in 18 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.587× (z -5.4, q 3e-05, down in 12 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NMRAL2P]] (+0.73, fdr 7e-06), [[NMRAL2P-1]] (+0.71, fdr 7e-06), [[PIR]] (+0.70, fdr 7e-06); moves opposite to [[RSRP1]] (-0.47, fdr 3e-05), [[FAM76B]] (-0.45, fdr 4e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 24 go from it, the strongest it → [[FBXW10B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10183.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **4.57×** | +14.5 | 6e-45 | 18/18 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.09×** | +14.2 | 1e-43 | 17/18 (HEC-1-A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.83×** | +13.6 | 9e-40 | 13/18 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.62×** | +13.0 | 2e-36 | 18/18 (HEC-1-A, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.13×** | +11.1 | 1e-26 | 2/8 (NCI-H1573, HEC-1-A) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.88×** | +9.9 | 5e-21 | 2/10 (NCI-H1573, A549) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.25×** | +8.2 | 2e-14 | 3/13 (NCI-H1573, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.94×** | +7.3 | 3e-11 | 9/13 (HEC-1-A, LS 180, …) | all doses, flat | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.19×** | +5.6 | 1e-06 | 10/18 (HepG2/C3A, H4, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +5.1 | 2e-05 | 6/17 (NCI-H1573, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.46×** | +4.8 | 1e-04 | 2/10 (HEC-1-A, CFPAC-1) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.1 | 0.002 | 0/14 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.005 | 0/18 | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.45×** | +3.8 | 0.006 | 5/18 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.009 | 2/15 (CFPAC-1, LoVo) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.009 | 5/18 (NCI-H2030, A549, …) | top dose only |  |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.42×** | +3.6 | 0.013 | 4/18 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.40×** | +3.4 | 0.024 | 9/18 (LS 180, HCT15, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.037 | 3/18 (LS 180, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~7% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.037 | 4/17 (NCI-H1573, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.51×** | +2.9 | 0.077 | 2/17 (Hs 766T, HepG2/C3A) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.34×** | +2.9 | 0.077 | 7/18 (HEC-1-A, NCI-H2030, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10183.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -5.4 | 3e-05 | 12/18 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.595×** | -5.3 | 4e-05 | 11/18 (NCI-H1573, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.600×** | -5.2 | 4e-05 | 11/18 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -4.7 | 3e-04 | 7/18 (SW1417, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.702×** | -3.3 | 0.093 | 0/18 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10183. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 20.5 | 1 | 9 (6 ⚠) | [[Auranofin (drug)]] 5 µM 4.46× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.1) |
| [[HEC-1-A (line)]] | alt | 38.6 | 3 | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 4.19× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -16.6) |
| [[SW1417 (line)]] | alt | 26.3 | 2 | 4 (3 ⚠) | [[Auranofin (drug)]] 5 µM 4.25× (z +9.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -13.3) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.222× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 32.0 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +14.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.256× (z -10.2) ⚠ cell-cycle shift, explains ~21% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.173× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 10.9 | 3 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 10.2× (z +11.0) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0978× (z -10.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[CFPAC-1 (line)]] | alt | 5.64 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +12.9) | — |
| [[LoVo (line)]] | wt | 4.20 | 2 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.25× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 12.2 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.113× (z -8.9) |
| [[A498 (line)]] | wt | 45.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.395× (z -9.2) ⚠ cell-cycle shift, explains ~24% of this change |
| [[HepG2_C3A (line)]] | wt | 4.81 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 21.9× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 7.52 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -10.8) ⚠ cell-cycle shift, explains ~21% of this change |
| [[KATO III (line)]] | alt | 7.45 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 32.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.01× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.73 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.681 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.832 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.572 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.824 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.868 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.658 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.644 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.92 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.829 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.694 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.846 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.798 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.654 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10183), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NMRAL2P]] | +0.73 | +0.68 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[NMRAL2P-1]] | +0.71 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[PIR]] | +0.70 | +0.66 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[EGF]] | +0.69 | +0.59 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[TRIM16L]] | +0.67 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[GCLM]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 | pathway: Biological oxidations |
| [[SLC7A11]] | +0.64 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[ME1]] | +0.63 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[VEGFD]] | +0.63 | +0.58 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[TXNRD1]] | +0.62 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[EID3]] | +0.61 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[AKR1C1]] | +0.59 | +0.58 / +0.61 | both halves | 8e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RSRP1]] | -0.47 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[FAM76B]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises CYP4F11's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[CYP4F3]] | C | CYP4F3 activity raises CYP4F11's level | lines that do not express CYP4F3 (29) vs lines expressing it (21) | 3.70× lower at baseline in the lines without CYP4F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: P2RY2, CYP3A5, ITGB6; co-absent with the target |
| [[LINC01564]] | C | LINC01564 activity raises CYP4F11's level | lines that do not express LINC01564 (24) vs lines expressing it (26) | 3.88× lower at baseline in the lines without LINC01564 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC03040, INAVA, CYP4F11; maybe low, not absent; co-absent with the target |
| [[LINP1]] | C | LINP1 activity raises CYP4F11's level | lines that do not express LINP1 (29) vs lines expressing it (21) | 2.80× lower at baseline in the lines without LINP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285743, LINC00707, IGFN1; co-absent with the target |
| [[STON2]] | C | STON2 activity raises CYP4F11's level | lines that do not express STON2 (19) vs lines expressing it (31) | 2.76× lower at baseline in the lines without STON2 | 0.016 | ⚠ within organs, on part of the lines; also absent: FRK, RASSF6, AQP3; co-absent with the target |
| [[NMRAL2P]] | C | NMRAL2P activity raises CYP4F11's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 2.57× lower at baseline in the lines without NMRAL2P | 0.022 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1; co-absent with the target |
| [[NMRAL2P-1]] | C | NMRAL2P-1 activity raises CYP4F11's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 2.59× lower at baseline in the lines without NMRAL2P-1 | 0.024 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1; co-absent with the target |
| [[AKR1C3]] | C | AKR1C3 activity raises CYP4F11's level | lines that do not express AKR1C3 (19) vs lines expressing it (31) | 2.42× lower at baseline in the lines without AKR1C3 | 0.034 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, HNF1A, SLC22A3; co-absent with the target |
| [[ALOX12P2-1]] | C | ALOX12P2-1 activity raises CYP4F11's level | lines that do not express ALOX12P2-1 (29) vs lines expressing it (21) | 2.51× lower at baseline in the lines without ALOX12P2-1 | 0.045 | ⚠ within organs, on part of the lines; also absent: NID2, MEG8, UNC5D; maybe low, not absent; co-absent with the target |
| [[LINC01589]] | C | LINC01589 activity raises CYP4F11's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 2.75× lower at baseline in the lines without LINC01589 | 0.053 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A; co-absent with the target |
| [[CRYBG2]] | C | CRYBG2 activity raises CYP4F11's level | lines that do not express CRYBG2 (23) vs lines expressing it (27) | 2.04× lower at baseline in the lines without CRYBG2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: SPINT1-AS1, SMPDL3B, LAD1; co-absent with the target |

### Downstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 7, C 17. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FBXW10B]] | B | CYP4F11 activity raises FBXW10B's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without CYP4F11 | 0.004 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[GCLC]] | B | CYP4F11 activity raises GCLC's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.21× lower at baseline in the lines without CYP4F11 | 0.019 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[TRIM16]] | B | CYP4F11 activity raises TRIM16's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 1.58× lower at baseline in the lines without CYP4F11 | 0.021 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[SLC7A11]] | B | CYP4F11 activity raises SLC7A11's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without CYP4F11 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[CAPS2]] | B | CYP4F11 activity weakens CAPS2's drug response | lines that do not express CYP4F11 (24) vs lines expressing it (13) | the lines without CYP4F11 respond 1.01× as strongly (z diff -0.01); strongest at Homoharringtonine 5 µM: 2.61x vs 0.79x (z diff -8.2) | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; target measured in part of the lines; both ways; artifact flags |
| [[NCF2]] | B | CYP4F11 activity raises NCF2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 1.89× lower at baseline in the lines without CYP4F11 | 0.076 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[ABCC2]] | B | CYP4F11 activity raises ABCC2's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without CYP4F11 | 0.085 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[ALOX12P2-1]] | C | CYP4F11 activity raises ALOX12P2-1's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.50× lower at baseline in the lines without CYP4F11 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[CYP4F3]] | C | CYP4F11 activity raises CYP4F3's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.69× lower at baseline in the lines without CYP4F11 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[LINC03040]] | C | CYP4F11 activity raises LINC03040's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.23× lower at baseline in the lines without CYP4F11 | 0.002 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[MAP7]] | C | CYP4F11 activity raises MAP7's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.34× lower at baseline in the lines without CYP4F11 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |
| [[AKR1C3]] | C | CYP4F11 activity raises AKR1C3's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without CYP4F11 | 0.003 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.806). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.3, 48.2); signed map (51.2, -10.1). **Vector** length 61.3, 17.7% of its response variance represented; |z| ≥ 3 in 451 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.55 to 8); *Nuclear events mediated by NFE2L2* (reactome, mean cos +0.60 to 7); *KEAP1-NFE2L2 pathway* (reactome, mean cos +0.60 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +5.4 | +14.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.1 | +13.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.1 | +14.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.4 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +2.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +5.6 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +1.3 | +3.8 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -1.8 | -1.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -4.7 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -1.2 | -1.3 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -2.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | cytochrome P450 family 4 subfamily F member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.12 — chr19:15,912,367-15,934,867 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Cytochrome P450 family 4 |
| Hallmark sets | ESTROGEN_RESPONSE_LATE |
| Reactome | 10 pathways, smallest: Fatty acids; Miscellaneous substrates; Eicosanoids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HBI6](https://www.uniprot.org/uniprotkb/Q9HBI6) (Cytochrome P450 4F11):

> A cytochrome P450 monooxygenase involved in the metabolism of various endogenous substrates, including fatty acids and their oxygenated derivatives (oxylipins). Mechanistically, uses molecular oxygen inserting one oxygen atom into a substrate, and reducing the second into a water molecule, with two electrons provided by NADPH via cytochrome P450 reductase (CPR; NADPH-ferrihemoprotein reductase). Catalyzes with high efficiency the oxidation of the terminal carbon (omega-oxidation) of 3-hydroxy …

**Summary**, from NCBI Gene [57834](https://www.ncbi.nlm.nih.gov/gene/57834):

> This gene, CYP4F11, encodes a member of the cytochrome P450 superfamily of enzymes. The cytochrome P450 proteins are monooxygenases which catalyze many reactions involved in drug metabolism and synthesis of cholesterol, steroids and other lipids. This gene is part of a cluster of cytochrome P450 genes on chromosome 19. Another member of this family, CYP4F2, is approximately 16 kb away. Alternatively spliced transcript variants encoding the same protein have been found for this gene. [provided …

**Accessions** — [HGNC:13265](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13265) · Entrez [57834](https://www.ncbi.nlm.nih.gov/gene/57834) · UniProt [Q9HBI6](https://www.uniprot.org/uniprotkb/Q9HBI6) · Ensembl [ENSG00000171903](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171903)

## Data

Gene col 10183: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10183); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10183, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10183]; `tensor/DDL_lfc|DDL_z.npy` [10183]; `embed/gene_vectors.npy` [10183]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10183 or target_col == 10183). Every well: [[CYP4F11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP4F11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
