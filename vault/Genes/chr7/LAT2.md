---
symbol: "LAT2"
type: "gene"
col: 1471
ensembl_id: "ENSG00000086730"
name: "linker for activation of T cells family member 2"
location: "7q11.23"
module: 47
arm: "+"
pooled_cpm: 10.42
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 21
n_dd_up_clean: 13
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/047"]
generated_by: "tahoemap"
---

# LAT2

*linker for activation of T cells family member 2* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.29× (z +13.3, q 1e-37, up in 30 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.04× (z +11.2, q 6e-27, up in 34 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (none with an alert); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.506× (z -6.9, q 2e-09, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MPP4]] (+0.74, fdr 7e-06), [[SLC22A14]] (+0.73, fdr 7e-06), [[SMIM41]] (+0.72, fdr 7e-06).
> It is in [[Module 047]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1471.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.29×** | +13.3 | 1e-37 | 30/35 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +12.7 | 1e-34 | 16/20 (LoVo, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +11.2 | 6e-27 | 34/44 (AsPC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.43×** | +9.2 | 6e-18 | 19/24 (SW1417, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.68×** | +8.2 | 2e-14 | 22/42 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +7.9 | 3e-13 | 31/47 (A498, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +7.1 | 1e-10 | 24/42 (LoVo, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.85×** | +6.9 | 4e-10 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +6.9 | 4e-10 | 24/45 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.68×** | +5.8 | 4e-07 | 23/46 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +5.8 | 5e-07 | 22/47 (A498, NCI-H2347, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.33×** | +4.9 | 4e-05 | 7/41 (SW480, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.7 | 1e-04 | 17/40 (NCI-H1573, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.43×** | +3.8 | 0.007 | 12/47 (A498, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.87×** | +3.7 | 0.009 | 6/18 (NCI-H1573, A498, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.063 | 11/47 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.072 | 5/42 (HCT15, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +3.0 | 0.086 | 7/45 (A549, HepG2/C3A, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, none with an alert; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1471.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -6.9 | 2e-09 | 27/46 (A-427, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -6.6 | 1e-08 | 25/48 (HEC-1-A, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.584×** | -5.6 | 5e-06 | 23/47 (SW480, A549, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.397×** | -5.4 | 9e-06 | 16/40 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -5.0 | 6e-05 | 22/46 (H4, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.669×** | -4.5 | 6e-04 | 20/46 (hTERT-HPNE, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.755×** | -4.5 | 7e-04 | 15/47 (NCI-H2347, PANC-1, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.692×** | -4.1 | 0.003 | 17/47 (SW480, NCI-H1573, …) | all doses, flat |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **0.693×** | -3.9 | 0.006 | 13/45 (LoVo, KATO III, …) | inconsistent across doses | low cells (technical?) |
| [[Trametinib (drug)]] 5 µM |  | **0.712×** | -3.8 | 0.007 | 16/48 (SW480, HT-29, …) | all doses, flat | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **0.669×** | -3.8 | 0.007 | 15/46 (J82, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.763×** | -3.5 | 0.020 | 14/46 (SW 1271, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.020 | 14/45 (NCI-H2030, SW480, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.721×** | -3.5 | 0.022 | 6/46 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.810×** | -3.3 | 0.032 | 13/47 (SW480, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1471. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 15.1 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.12× (z +16.0) | [[Digitoxin (drug)]] 5 µM 0.208× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 22.8 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.174× (z -11.8) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.220× (z -10.6) |
| [[SW1417 (line)]] | alt | 15.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +11.8) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 14.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.88× (z +10.1) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.130× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 5.21 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0513× (z -10.3) |
| [[HCT15 (line)]] | alt | 27.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.35× (z +11.2) | — |
| [[HT-29 (line)]] | alt | 14.7 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.165× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 10.5 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 7.58× (z +9.9) ⚠ toxic | — |
| [[NCI-H1792 (line)]] | alt | 6.58 | 0 | 1 (1 ⚠) | — | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.0589× (z -9.5) ⚠ transcription drop; unreliable plate only |
| [[NCI-H23 (line)]] | alt | 10.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0947× (z -9.7) |
| [[SW480 (line)]] | alt | 23.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.96× (z +8.9) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.25 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.61 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.08 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.47 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.28 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 53.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1471), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MPP4]] | +0.74 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[SLC22A14]] | +0.73 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[SMIM41]] | +0.72 | +0.76 / +0.71 | both halves | 7e-06 |  |
| [[MIR9-1HG]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 |  |
| [[SELPLG]] | +0.72 | +0.74 / +0.65 | both halves | 7e-06 |  |
| [[LINC01588]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[NUP210L]] | +0.71 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[EPHX3]] | +0.71 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[MYOCOS]] | +0.71 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[CPT1C]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[FNDC7]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PITRM1-AS1]] | +0.71 | +0.74 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LAT2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DNAH17]] | B | DNAH17 activity raises LAT2's level | lines that do not express DNAH17 (13) vs lines expressing it (37) | 1.55× lower at baseline in the lines without DNAH17 | 0.036 | ⚠ within organs, on part of the lines; also absent: EPAS1, LINC03042, ENSG00000261227; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises LAT2's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.4% of all compounds | 0.067 | ⚠ off-target possible; 3 compounds |
| [[SCAT1]] | B | SCAT1 activity raises LAT2's level | lines that do not express SCAT1 (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without SCAT1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000266088, PDK4, ADGRE2; maybe low, not absent |
| [[IL19]] | B | IL19 activity raises LAT2's level | lines that do not express IL19 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without IL19 | 0.092 | ⚠ within organs, on part of the lines; also absent: PKHD1, IHO1, CASC20; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 047]]; 95 genes; every member is in the + arm (projection on the module's main direction 0.766). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (34.7, -15.5); signed map (14.8, 10.5). **Vector** length 96.3, 20.6% of its response variance represented; |z| ≥ 3 in 1,075 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.1 | +12.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.5 | +5.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +6.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.7 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.6 | +5.8 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -5.0 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.8 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.5 | -5.0 |
|  | [[NG25 (drug)]] 5 µM |  | -3.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.8 | -5.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.7 | -4.5 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.0 | -4.1 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.9 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | linker for activation of T cells family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:74,199,652-74,229,834 (+) |
| Ensembl biotype | protein_coding |
| Also known as | WSCR5, HSPC046, LAB, NTAL; previously WBSCR15, WBSCR5 |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 3 pathways, smallest: Role of LAT2/NTAL/LAB on calcium mobilization; Fc epsilon receptor (FCERI) signaling; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9GZY6](https://www.uniprot.org/uniprotkb/Q9GZY6) (Linker for activation of T-cells family member 2):

> Involved in FCER1 (high affinity immunoglobulin epsilon receptor)-mediated signaling in mast cells. May also be involved in BCR (B-cell antigen receptor)-mediated signaling in B-cells and FCGR1 (high affinity immunoglobulin gamma Fc receptor I)-mediated signaling in myeloid cells. Couples activation of these receptors and their associated kinases with distal intracellular events through the recruitment of GRB2.

**Summary**, from NCBI Gene [7462](https://www.ncbi.nlm.nih.gov/gene/7462):

> This gene is one of the contiguous genes at 7q11.23 commonly deleted in Williams syndrome, a multisystem developmental disorder. This gene consists of at least 14 exons, and its alternative splicing generates 3 transcript variants, all encoding the same protein. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:12749](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12749) · Entrez [7462](https://www.ncbi.nlm.nih.gov/gene/7462) · UniProt [Q9GZY6](https://www.uniprot.org/uniprotkb/Q9GZY6) · Ensembl [ENSG00000086730](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000086730)

## Data

Gene col 1471: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1471); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1471, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1471]; `tensor/DDL_lfc|DDL_z.npy` [1471]; `embed/gene_vectors.npy` [1471]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1471 or target_col == 1471). Every well: [[LAT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
