---
symbol: "VKORC1"
type: "gene"
col: 9465
ensembl_id: "ENSG00000167397"
name: "vitamin K epoxide reductase complex subunit 1"
location: "16p11.2"
module: 79
arm: "+"
pooled_cpm: 48.12
n_lines_expressing: 48
n_dd_up: 0
n_dd_down: 13
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 9
direction_downstream: 0
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# VKORC1

*vitamin K epoxide reductase complex subunit 1* — 16p11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.265× (z -14.6, q 1e-45, down in 44 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDT]] (+0.79, fdr 7e-06), [[HILPDA]] (+0.78, fdr 7e-06), [[WDR54]] (+0.77, fdr 7e-06); moves opposite to [[TRIM44]] (-0.70, fdr 7e-06), [[EWSR1]] (-0.68, fdr 1e-05), [[U2SURP]] (-0.68, fdr 7e-06).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SLC2A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

No drug-dose raises it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9465.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.265×** | -14.6 | 1e-45 | 44/46 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.252×** | -10.7 | 2e-24 | 45/46 (RPMI-7951, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.405×** | -6.7 | 5e-09 | 38/46 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.705×** | -3.9 | 0.016 | 30/46 (SNU-1, H4, …) | rises with dose | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.607×** | -3.7 | 0.023 | 35/45 (SW480, HEC-1-A, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.410×** | -3.6 | 0.023 | 37/46 (SNU-1, Hs 766T, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.612×** | -3.6 | 0.023 | 33/45 (HepG2/C3A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.659×** | -3.3 | 0.073 | 33/46 (HEC-1-A, C-33 A, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -3.2 | 0.073 | 28/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.662×** | -3.2 | 0.073 | 26/46 (NCI-H1792, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.462×** | -3.1 | 0.087 | 28/46 (RPMI-7951, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.672×** | -3.1 | 0.092 | 28/45 (SW 900, RPMI-7951, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.660×** | -3.1 | 0.099 | 25/46 (A-172, C32, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9465. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 65.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -11.8) |
| [[A-172 (line)]] | wt | 101 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.5) |
| [[C32 (line)]] | wt | 94.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -13.5) |
| [[CHP-212 (line)]] | wt | 42.2 | 0 | 2 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.0757× (z -9.5) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0826× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 35.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.6) |
| [[HepG2_C3A (line)]] | wt | 71.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -11.8) |
| [[HOP62 (line)]] | alt | 52.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -17.1) |
| [[HS-578T (line)]] | alt | 79.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 72.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -13.8) |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -11.2) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -12.1) |
| [[NCI-H460 (line)]] | wt | 49.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -14.2) |
| [[RKO (line)]] | wt | 47.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 96.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0391× (z -21.2) |
| [[SW 900 (line)]] | alt | 59.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.6) |
| [[SW48 (line)]] | wt | 32.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -12.9) |
| [[A-427 (line)]] | wt | 41.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0708× (z -17.1) |
| [[A498 (line)]] | wt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.3) |
| [[A549 (line)]] | wt | 48.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -13.6) |
| [[AN3 CA (line)]] | alt | 64.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.139× (z -9.4) |
| [[BT-474 (line)]] | alt | 25.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.1) |
| [[C-33 A (line)]] | alt | 71.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -11.9) |
| [[CFPAC-1 (line)]] | alt | 52.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -10.3) |
| [[H4 (line)]] | wt | 56.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -11.4) |
| [[HCT15 (line)]] | alt | 38.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -16.3) |
| [[Hs 766T (line)]] | wt | 48.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 72.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -10.8) |
| [[J82 (line)]] | alt | 76.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.0) |
| [[LOX-IMVI (line)]] | wt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.142× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 64.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 77.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.5) |
| [[PANC-1 (line)]] | alt | 51.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.9) |
| [[SNU-1 (line)]] | wt | 46.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -10.9) |
| [[SNU-423 (line)]] | alt | 67.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -16.3) |
| [[SW 1088 (line)]] | alt | 84.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -8.5) |
| [[SW 1271 (line)]] | alt | 58.6 | 0 | 1 | — | [[Gemfibrozil (drug)]] 0.05 µM 0.0594× (z -9.0) |
| [[SW480 (line)]] | alt | 20.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -10.6) |
| [[AsPC-1 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9465), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDT]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.78 | +0.78 / +0.70 | both halves | 7e-06 |  |
| [[WDR54]] | +0.77 | +0.77 / +0.70 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.74 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[GPR155]] | +0.72 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[STK32C]] | +0.72 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[AKR7A2]] | +0.72 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[EFNA3]] | +0.72 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[UBE2O]] | +0.72 | +0.74 / +0.58 | both halves | 7e-06 |  |
| [[ABCB9]] | +0.72 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRIM44]] | -0.70 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[EWSR1]] | -0.68 | -0.50 / -0.69 | both halves | 1e-05 |  |
| [[U2SURP]] | -0.68 | -0.60 / -0.62 | both halves | 7e-06 |  |
| [[SFPQ]] | -0.67 | -0.57 / -0.71 | both halves | 9e-06 |  |
| [[ZNF655]] | -0.65 | -0.49 / -0.60 | both halves | 1e-05 |  |
| [[C22orf46]] | -0.65 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[ARMCX4]] | -0.65 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[UTP20]] | -0.64 | -0.63 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC2A3]] | B | SLC2A3 activity raises VKORC1's level | lines that do not express SLC2A3 (15) vs lines expressing it (35) | 1.94× lower at baseline in the lines without SLC2A3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SLC16A2, DPY19L2P2-1, LGALS1 |
| [[A1BG]] | B | A1BG activity raises VKORC1's level | lines that do not express A1BG (17) vs lines expressing it (33) | 1.83× lower at baseline in the lines without A1BG | 0.031 | ⚠ within organs, on part of the lines; also absent: A1BG-AS1, NPTX1, DZIP1 |
| [[LIX1L]] | B | LIX1L activity raises VKORC1's level | lines that do not express LIX1L (10) vs lines expressing it (38) | 2.61× lower at baseline in the lines without LIX1L | 0.031 | ⚠ within organs, on part of the lines; also absent: CCDC88A, GIHCG, BOLA3-DT |
| [[LINC03047]] | B | LINC03047 activity raises VKORC1's level | lines that do not express LINC03047 (28) vs lines expressing it (22) | 1.81× lower at baseline in the lines without LINC03047 | 0.044 | ⚠ within organs, on part of the lines; also absent: CNRIP1, ITGA4, INSYN2B |
| [[CLEC2B]] | B | CLEC2B activity raises VKORC1's level | lines that do not express CLEC2B (22) vs lines expressing it (28) | 1.70× lower at baseline in the lines without CLEC2B | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, TMEM158, FRMD4A |
| [[HTR1D]] | B | HTR1D activity lowers VKORC1's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 1.25× higher at baseline in the lines without HTR1D | 0.096 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[LGALS1]] | B | LGALS1 activity raises VKORC1's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.06× lower at baseline in the lines without LGALS1 | 0.097 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[CLTCL1]] | C | CLTCL1 activity raises VKORC1's level | lines that do not express CLTCL1 (3) vs lines expressing it (47) | 3.06× lower at baseline in the lines without CLTCL1 | 0.023 | ⚠ few lines (3 vs 47); across organs; also absent: NKAIN1, WHRN, SUGCT |
| [[IKBIP]] | C | IKBIP activity raises VKORC1's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.804). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.8, -14.9); signed map (-35.0, 22.0). **Vector** length 107, 38.0% of its response variance represented; |z| ≥ 3 in 565 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.54 to 16); *hypoxia* (control, mean cos +0.63 to 5); *glycolysis* (hallmark, mean cos +0.59 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | -1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.4 | -3.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.1 | -0.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.5 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.1 | +0.3 |
|  | [[Sinomenine (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +1.9 | +0.7 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +1.8 | +1.4 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.3 | +0.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.8 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.7 | -0.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.1 | -3.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -5.3 | -3.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.9 | -1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.8 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | vitamin K epoxide reductase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p11.2 — chr16:31,090,842-31,095,980 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously VKCFD2 |
| Gene groups (HGNC) | Vitamin K epoxide reductase complex subunit 1 family |
| Reactome | 3 pathways, smallest: Metabolism of vitamin K; Metabolism of fat-soluble vitamins; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQB6](https://www.uniprot.org/uniprotkb/Q9BQB6) (Vitamin K epoxide reductase complex subunit 1):

> Involved in vitamin K metabolism. Catalytic subunit of the vitamin K epoxide reductase (VKOR) complex which reduces inactive vitamin K 2,3-epoxide to active vitamin K. Vitamin K is required for the gamma-carboxylation of various proteins, including clotting factors, and is required for normal blood coagulation, but also for normal bone development.

**Summary**, from NCBI Gene [79001](https://www.ncbi.nlm.nih.gov/gene/79001):

> This gene encodes the catalytic subunit of the vitamin K epoxide reductase complex, which is responsible for the reduction of inactive vitamin K 2,3-epoxide to active vitamin K in the endoplasmic reticulum membrane. Vitamin K is a required co-factor for carboxylation of glutamic acid residues by vitamin K-dependent gamma-carboxylase in blood-clotting enzymes. Allelic variation in this gene is associated with vitamin k-dependent clotting factors combined deficiency of 2, and increased resistance …

**Accessions** — [HGNC:23663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23663) · Entrez [79001](https://www.ncbi.nlm.nih.gov/gene/79001) · UniProt [Q9BQB6](https://www.uniprot.org/uniprotkb/Q9BQB6) · Ensembl [ENSG00000167397](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167397)

## Data

Gene col 9465: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9465); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9465, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9465]; `tensor/DDL_lfc|DDL_z.npy` [9465]; `embed/gene_vectors.npy` [9465]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9465 or target_col == 9465). Every well: [[VKORC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VKORC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
