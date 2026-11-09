---
symbol: "PKN3"
type: "gene"
col: 8352
ensembl_id: "ENSG00000160447"
name: "protein kinase N3"
location: "9q34.11"
module: 71
arm: "+"
pooled_cpm: 10.17
n_lines_expressing: 46
n_dd_up: 14
n_dd_down: 10
n_dd_up_clean: 11
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# PKN3

*protein kinase N3* — 9q34.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Ipatasertib (drug)]] 0.5 µM: 1.66× (z +5.3, q 7e-05, up in 16 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.459× (z -11.5, q 1e-27, down in 35 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MSI1]] (+0.64, fdr 1e-05), [[GINS3]] (+0.60, fdr 4e-05), [[ADCY3]] (+0.58, fdr 1e-05); moves opposite to [[ECHS1]] (-0.52, fdr 3e-04), [[PJA2]] (-0.52, fdr 5e-05), [[GDE1]] (-0.50, fdr 1e-04).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 2 go from it, the strongest it → [[LIN9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8352.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.66×** | +5.3 | 7e-05 | 16/37 (RKO, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +4.2 | 0.009 | 17/38 (A498, BT-474, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.068 | 4/38 (SW480, SK-MEL-2, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.5 | 0.068 | 10/42 (SW480, H4, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +3.4 | 0.068 | 4/42 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.18× | +3.4 | 0.068 | 7/43 (A498, SNU-1, …) | top dose only |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.37×** | +3.3 | 0.068 | 2/39 (SW480, A498) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **1.25×** | +3.2 | 0.068 | 7/32 (LoVo, LS 180, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.2 | 0.068 | 6/43 (HCT15, SW480, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.36×** | +3.2 | 0.068 | 5/39 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ritonavir (drug)]] 5 µM |  | 1.17× | +3.2 | 0.068 | 7/43 (SW1417, HepG2/C3A, …) | top dose only |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +3.2 | 0.068 | 0/19 | top dose only | noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.068 | 3/39 (PANC-1, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.1 | 0.069 | 16/35 (A-427, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.085 | 7/41 (CFPAC-1, A549, …) | rises with dose |  |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.23×** | +3.0 | 0.087 | 2/43 (LoVo, SNU-423) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.459×** | -11.5 | 1e-27 | 35/43 (SW480, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.498×** | -10.3 | 3e-22 | 28/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.514×** | -9.8 | 2e-20 | 26/43 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.622×** | -7.0 | 4e-10 | 25/43 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.719×** | -4.9 | 1e-04 | 14/38 (SK-MEL-2, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.725×** | -4.7 | 2e-04 | 16/43 (MIA PaCa-2, A-172, …) | top dose only | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.501×** | -4.7 | 2e-04 | 11/42 (SW1417, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.806×** | -4.5 | 5e-04 | 18/40 (MIA PaCa-2, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.039 | 15/40 (SNU-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.061 | 11/38 (SW48, CFPAC-1, …) | top dose only |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | 0.805× | -3.0 | 0.12 | 0/43 | two highest doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 33.7 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.0650× (z -32.6) |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.146× (z -14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.335× (z -8.8) |
| [[SNU-1 (line)]] | wt | 32.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0835× (z -12.9) |
| [[SW480 (line)]] | alt | 13.8 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.226× (z -12.3) |
| [[Hs 766T (line)]] | wt | 27.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.220× (z -9.7) |
| [[SW48 (line)]] | wt | 15.6 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0970× (z -9.5) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.224× (z -11.2) |
| [[AsPC-1 (line)]] | alt | 3.15 | 0 | 1 | — | [[Vortioxetine (drug)]] 0.5 µM 0.0391× (z -10.3) |
| [[NCI-H2030 (line)]] | alt | 9.29 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.147× (z -11.1) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 9.08 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.176× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[RKO (line)]] | wt | 54.8 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.344× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 6.54 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.0973× (z -9.4) |
| [[A-427 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.76 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.20 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.15 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.95 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MSI1]] | +0.64 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[GINS3]] | +0.60 | +0.40 / +0.53 | both halves | 4e-05 |  |
| [[ADCY3]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SFMBT1]] | +0.58 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[SUZ12P1]] | +0.58 | +0.45 / +0.50 | both halves | 3e-05 |  |
| [[HDAC7]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TYRO3]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[LIN9]] | +0.56 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[IGHMBP2]] | +0.55 | +0.44 / +0.50 | both halves | 3e-05 |  |
| [[KCNQ4]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[GABPB1]] | +0.54 | +0.37 / +0.43 | both halves | 8e-05 |  |
| [[TNPO2]] | +0.54 | +0.41 / +0.50 | both halves | 4e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECHS1]] | -0.52 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[PJA2]] | -0.52 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[GDE1]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[ACP1]] | -0.47 | -0.38 / -0.49 | both halves | 6e-05 |  |
| [[TMEM30A]] | -0.47 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[TMED7]] | -0.46 | -0.30 / -0.48 | both halves | 2e-04 |  |
| [[MDH1]] | -0.46 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[MAGT1]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[CAST]] | -0.46 | -0.32 / -0.35 | both halves | 2e-04 |  |
| [[LAMP2]] | -0.45 | -0.29 / -0.58 | both halves | 2e-04 |  |
| [[VAMP7]] | -0.45 | -0.26 / -0.42 | both halves | 4e-04 |  |
| [[ATP7A]] | -0.45 | -0.38 / -0.42 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises PKN3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.67× lower at baseline in the lines without MSI1 | 0.009 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[TBX1]] | B | TBX1 activity raises PKN3's level | lines that do not express TBX1 (23) vs lines expressing it (27) | 1.62× lower at baseline in the lines without TBX1 | 0.030 | ⚠ within organs, on part of the lines; also absent: BEGAIN, PALM, OLFM1 |
| [[FAXC]] | B | FAXC activity raises PKN3's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without FAXC | 0.037 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ULK2]] | B | ULK2 activity raises PKN3's level | lines that do not express ULK2 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without ULK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: ANKRD6, TRABD2B, HOMER2 |
| [[FGD1]] | B | FGD1 activity raises PKN3's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.01× lower at baseline in the lines without FGD1 | 0.083 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[HDAC6]] | B | HDAC6 activity raises PKN3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LIN9]] | C | PKN3 activity raises LIN9's level | lines that do not express PKN3 (4) vs lines expressing it (46) | 1.68× lower at baseline in the lines without PKN3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUDT7, ITPKA, DNM1; maybe low, not absent; its own permutation p |
| [[TYRO3]] | C | PKN3 activity raises TYRO3's level | lines that do not express PKN3 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without PKN3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NUDT7, ITPKA, DNM1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.477). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, 11.7); signed map (6.1, -2.9). **Vector** length 61.1, 9.81% of its response variance represented; |z| ≥ 3 in 760 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.6 | +4.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.3 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.6 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.2 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.0 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.6 | +1.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +1.3 |
| fall | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -2.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.4 | -4.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.2 | -11.5 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -3.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.1 | -2.4 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | protein kinase N3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q34.11 — chr9:128,702,503-128,720,916 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PKNbeta, UTDP4-1 |
| Gene groups (HGNC) | C2 domain containing protein kinases; Minor histocompatibility antigens; Protein kinase N family |
| Reactome | 8 pathways, smallest: RHO GTPases activate PKNs; RHOB GTPase cycle; RHOC GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6P5Z2](https://www.uniprot.org/uniprotkb/Q6P5Z2) (Serine/threonine-protein kinase N3):

> Contributes to invasiveness in malignant prostate cancer.

**Summary**, from NCBI Gene [29941](https://www.ncbi.nlm.nih.gov/gene/29941):

> Predicted to enable protein serine/threonine kinase activity. Involved in epithelial cell migration. Predicted to be located in Golgi apparatus; cytosol; and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17999) · Entrez [29941](https://www.ncbi.nlm.nih.gov/gene/29941) · UniProt [Q6P5Z2](https://www.uniprot.org/uniprotkb/Q6P5Z2) · Ensembl [ENSG00000160447](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160447)

## Data

Gene col 8352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8352); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8352]; `tensor/DDL_lfc|DDL_z.npy` [8352]; `embed/gene_vectors.npy` [8352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8352 or target_col == 8352). Every well: [[PKN3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKN3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
