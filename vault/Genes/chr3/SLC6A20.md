---
symbol: "SLC6A20"
type: "gene"
col: 8787
ensembl_id: "ENSG00000163817"
name: "solute carrier family 6 member 20"
location: "3p21.31"
module: 73
arm: "+"
pooled_cpm: 15.48
n_lines_expressing: 12
n_dd_up: 15
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 101
direction_downstream: 83
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SLC6A20

*solute carrier family 6 member 20* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.76× (z +19.4, q 0e+00, up in 1 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.545× (z -6.3, q 2e-07, down in 8 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HEPH]] (+0.85, fdr 7e-06), [[NPSR1]] (+0.84, fdr 7e-06), [[DSG4]] (+0.83, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 101 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 83 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8787.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.76×** | +19.4 | 0e+00 | 1/10 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.95×** | +6.9 | 1e-09 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +6.9 | 1e-09 | 3/8 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +6.3 | 5e-08 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +5.4 | 7e-06 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 4e-05 | 1/10 (SW 900) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.40×** | +4.9 | 7e-05 | 1/10 (HCT15) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.59×** | +4.8 | 1e-04 | 4/10 (HT-29, Panc 03.27, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.89×** | +4.7 | 1e-04 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +4.2 | 0.001 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.41×** | +3.6 | 0.017 | 4/10 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.41×** | +3.6 | 0.017 | 4/10 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.4 | 0.026 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.062 | 1/10 (Panc 03.27) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.77×** | +3.1 | 0.080 | 0/4 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8787.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.545×** | -6.3 | 2e-07 | 8/10 (AsPC-1, LS 180, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.595×** | -5.1 | 8e-05 | 9/10 (LS 180, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.620×** | -4.9 | 2e-04 | 9/10 (LS 180, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.629×** | -4.8 | 3e-04 | 4/10 (LS 180, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.668×** | -4.2 | 0.004 | 6/10 (LS 180, LoVo, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.784×** | -3.5 | 0.039 | 4/10 (LoVo, LS 180, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.716×** | -3.4 | 0.045 | 7/10 (HT-29, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.717×** | -3.4 | 0.045 | 6/10 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.725×** | -3.3 | 0.059 | 7/10 (LoVo, LS 180, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.559×** | -3.1 | 0.091 | 6/10 (LoVo, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.738×** | -3.1 | 0.091 | 6/10 (LoVo, Panc 03.27, …) | top dose only |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.741×** | -3.1 | 0.097 | 1/10 (AsPC-1) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8787. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 218 | 0 | 11 (10 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0348× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -17.5) |
| [[LS 180 (line)]] | wt | 93.4 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0901× (z -22.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0668× (z -17.7) |
| [[AsPC-1 (line)]] | alt | 96.9 | 0 | 10 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0457× (z -20.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.1) |
| [[SW48 (line)]] | wt | 33.6 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -13.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0982× (z -9.4) |
| [[HT-29 (line)]] | alt | 18.0 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0724× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 30.0 | 0 | 3 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0685× (z -15.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[Panc 03.27 (line)]] | alt | 21.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0924× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 3.88 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0527× (z -8.5) |
| [[SW1417 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.42 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.15 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.67 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.45 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.31 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.97 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.44 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.53 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8787), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEPH]] | +0.85 | +0.81 / +0.81 | both halves | 7e-06 | pathway: Disorders of transmembrane transporters |
| [[NPSR1]] | +0.84 | +0.80 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[DSG4]] | +0.83 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SPON1]] | +0.81 | +0.79 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.81 | +0.76 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.80 | +0.82 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.76 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[LINC02474]] | +0.79 | +0.75 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[CLIC5]] | +0.78 | +0.83 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.77 | +0.71 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[TPRXL]] | +0.77 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[DSG3]] | +0.76 | +0.76 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*101 arrows, 101 of them with an alert ⚠; grade A 0, B 5, C 96. Shown: the 12 strongest; 89 more arrows (89 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC6A20's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NOSTRIN]] | B | NOSTRIN activity raises SLC6A20's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.61× lower at baseline in the lines without NOSTRIN | 0.059 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[CD55]] | B | CD55 activity raises SLC6A20's level | lines that do not express CD55 (16) vs lines expressing it (34) | 2.33× lower at baseline in the lines without CD55 | 0.070 | ⚠ within organs, on part of the lines; also absent: IL32, IL2RG, ENSG00000271933; maybe low, not absent |
| [[TJP2]] | B | TJP2 activity raises SLC6A20's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.47× lower at baseline in the lines without TJP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[IGSF9]] | B | IGSF9 activity raises SLC6A20's level | lines that do not express IGSF9 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without IGSF9 | 0.080 | ⚠ within organs, on part of the lines; also absent: DUSP4, CREG2, LYPD3 |
| [[LGR6]] | C | LGR6 activity raises SLC6A20's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.64× lower at baseline in the lines without LGR6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[PTPRR]] | C | PTPRR activity raises SLC6A20's level | lines that do not express PTPRR (32) vs lines expressing it (18) | 3.66× lower at baseline in the lines without PTPRR | 0.001 | ⚠ within organs, on part of the lines; also absent: DHRS9, LINC01133, TFF2; co-absent with the target |
| [[REG4]] | C | REG4 activity raises SLC6A20's level | lines that do not express REG4 (43) vs lines expressing it (7) | 11.64× lower at baseline in the lines without REG4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[FGFBP1]] | C | FGFBP1 activity raises SLC6A20's level | lines that do not express FGFBP1 (36) vs lines expressing it (14) | 5.57× lower at baseline in the lines without FGFBP1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL17A1, KLK10, SERPINB5; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises SLC6A20's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 6.07× lower at baseline in the lines without KLK10 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |
| [[HEPH]] | C | HEPH activity raises SLC6A20's level | lines that do not express HEPH (41) vs lines expressing it (9) | 7.85× lower at baseline in the lines without HEPH | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, HEPHL1, REG4; co-absent with the target |
| [[ST14]] | C | ST14 activity raises SLC6A20's level | lines that do not express ST14 (32) vs lines expressing it (18) | 4.88× lower at baseline in the lines without ST14 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMPRSS4, TMEM125, CDH1; co-absent with the target |

### Downstream of this gene

*83 arrows, 83 of them with an alert ⚠; grade A 0, B 24, C 59. Shown: the 12 strongest; 71 more arrows (71 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | SLC6A20 activity raises ANXA11's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.45× lower at baseline in the lines without SLC6A20 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[ADAP1]] | B | SLC6A20 activity raises ADAP1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.64× lower at baseline in the lines without SLC6A20 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[IL22RA1]] | B | SLC6A20 activity raises IL22RA1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.45× lower at baseline in the lines without SLC6A20 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[EPS8L1]] | B | SLC6A20 activity raises EPS8L1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.27× lower at baseline in the lines without SLC6A20 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[B4GALNT3]] | B | SLC6A20 activity raises B4GALNT3's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.59× lower at baseline in the lines without SLC6A20 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[GRHL3]] | B | SLC6A20 activity raises GRHL3's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.15× lower at baseline in the lines without SLC6A20 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[BAG1]] | B | SLC6A20 activity raises BAG1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 2.00× lower at baseline in the lines without SLC6A20 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[MUC12]] | B | SLC6A20 activity raises MUC12's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 2.92× lower at baseline in the lines without SLC6A20 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[TNFRSF21]] | B | SLC6A20 activity raises TNFRSF21's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 4.64× lower at baseline in the lines without SLC6A20 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[ABHD11]] | B | SLC6A20 activity raises ABHD11's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 2.95× lower at baseline in the lines without SLC6A20 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[NOSTRIN]] | B | SLC6A20 activity raises NOSTRIN's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 3.67× lower at baseline in the lines without SLC6A20 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |
| [[YOD1]] | B | SLC6A20 activity raises YOD1's level | lines that do not express SLC6A20 (38) vs lines expressing it (12) | 2.22× lower at baseline in the lines without SLC6A20 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KLK11, REG4, HEPH |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.873). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.1, 50.5); signed map (65.4, 7.9). **Vector** length 68.0, 36.0% of its response variance represented; |z| ≥ 3 in 317 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +6.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +4.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.8 | +19.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.0 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +0.7 | -0.2 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +0.7 | +0.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.7 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -1.4 | -6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -2.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | +0.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -1.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -2.5 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -0.7 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -0.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 20 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,755,449-45,796,574 (-) |
| Ensembl biotype | protein_coding |
| Also known as | XT3, Xtrp3, SIT1, IMINO |
| Gene groups (HGNC) | Solute carrier family 6 |
| Reactome | 7 pathways, smallest: SLC-mediated transport of neurotransmitters; Amino acid transport across the plasma membrane; SLC-mediated transport of amino acids |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NP91](https://www.uniprot.org/uniprotkb/Q9NP91) (Sodium- and chloride-dependent transporter XTRP3):

> Mediates the Na(+)- and Cl(-)-dependent uptake of imino acids such as L-proline, N-methyl-L-proline and pipecolate as well as N-methylated amino acids. Also transports glycine, regulates proline and glycine homeostasis in the brain playing a role in the modulation of NMDAR currents.

**Summary**, from NCBI Gene [54716](https://www.ncbi.nlm.nih.gov/gene/54716):

> Transport of small hydrophilic substances across cell membranes is mediated by substrate-specific transporter proteins which have been classified into several families of related genes. The protein encoded by this gene belongs to the sodium:neurotransmitter symporter (SNF) family and functions as a proline transporter expressed in kidney and small intestine. Mutations in this gene are associated with Hyperglycinuria and Iminoglycinuria. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:30927](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30927) · Entrez [54716](https://www.ncbi.nlm.nih.gov/gene/54716) · UniProt [Q9NP91](https://www.uniprot.org/uniprotkb/Q9NP91) · Ensembl [ENSG00000163817](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163817)

## Data

Gene col 8787: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8787); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8787, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8787]; `tensor/DDL_lfc|DDL_z.npy` [8787]; `embed/gene_vectors.npy` [8787]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8787 or target_col == 8787). Every well: [[SLC6A20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
