---
symbol: "PMS2CL"
type: "gene"
col: 11959
ensembl_id: "ENSG00000187953"
name: "PMS2 C-terminal like (pseudogene)"
location: "7p22.1"
module: 164
arm: "+"
pooled_cpm: 10.78
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 16
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# PMS2CL

*PMS2 C-terminal like (pseudogene)* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.94× (z +10.3, q 3e-22, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.442× (z -8.3, q 4e-14, down in 27 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Busulfan (drug)]] 0.05 µM: 0.645× (z -4.5, q 0.002, down in 22 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POM121C]] (+0.67, fdr 2e-05), [[TRMU]] (+0.63, fdr 7e-06), [[TRIT1]] (+0.62, fdr 7e-06); moves opposite to [[PDLIM5]] (-0.61, fdr 3e-05), [[DDX5]] (-0.58, fdr 7e-06), [[TJP1]] (-0.58, fdr 2e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[RRAGD]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11959.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.94×** | +10.3 | 3e-22 | 42/48 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.91×** | +7.3 | 1e-10 | 33/44 (SW480, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.98×** | +7.0 | 6e-10 | 32/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.67×** | +5.3 | 2e-05 | 26/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.61×** | +4.8 | 1e-04 | 20/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.0 | 0.006 | 18/48 (MIA PaCa-2, A-427, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.43×** | +3.6 | 0.024 | 13/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tomivosertib (drug)]] 5 µM |  | **1.84×** | +3.3 | 0.081 | 9/46 (PANC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.12 | 11/47 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 10 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11959.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.442×** | -8.3 | 4e-14 | 27/36 (SHP-77, NCI-H2347, …) | all doses, flat | composition shift |
| [[Busulfan (drug)]] 0.05 µM |  | **0.645×** | -4.5 | 0.002 | 22/48 (MIA PaCa-2, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.652×** | -4.4 | 0.002 | 22/48 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.656×** | -4.3 | 0.002 | 23/48 (KATO III, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.648×** | -4.1 | 0.005 | 15/28 (NCI-H2347, NCI-H2030, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.673×** | -4.1 | 0.005 | 21/48 (NCI-H2347, C32, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.666×** | -4.0 | 0.005 | 18/40 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~23% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.742×** | -3.9 | 0.006 | 16/48 (HOP62, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **0.671×** | -3.9 | 0.006 | 12/21 (CFPAC-1, H4, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.699×** | -3.7 | 0.014 | 16/48 (SW 1088, A-172, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.701×** | -3.5 | 0.025 | 18/46 (SNU-423, NCI-H23, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.713×** | -3.5 | 0.025 | 15/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.714×** | -3.4 | 0.025 | 15/48 (HOP62, HS-578T, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.715×** | -3.4 | 0.025 | 15/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.738×** | -3.1 | 0.072 | 20/42 (HOP62, HepG2/C3A, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~14% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11959. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0913× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[C32 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.127× (z -8.7) ⚠ cell-cycle shift, explains ~13% of this change |
| [[CFPAC-1 (line)]] | alt | 9.46 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0521× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change |
| [[HCT15 (line)]] | alt | 15.2 | 0 | 1 | — | [[Raltitrexed (drug)]] 0.5 µM 0.0892× (z -9.5) |
| [[J82 (line)]] | alt | 7.21 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.149× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 9.91 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.145× (z -9.7) ⚠ cell-cycle shift, explains ~35% of this change |
| [[PANC-1 (line)]] | alt | 14.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.0× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.125× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0831× (z -11.2) ⚠ cell-cycle shift, explains ~35% of this change |
| [[A-172 (line)]] | wt | 5.60 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11959), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POM121C]] | +0.67 | +0.78 / +0.48 | both halves | 2e-05 |  |
| [[TRMU]] | +0.63 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[TRIT1]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[SNAPC3]] | +0.61 | +0.74 / +0.53 | both halves | 1e-05 |  |
| [[HDHD5]] | +0.61 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[ZNF14]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SFXN1]] | +0.61 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[PMS2P3]] | +0.60 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[PEX3]] | +0.60 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[FNTB]] | +0.60 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[AKAP10]] | +0.59 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SMN1]] | +0.59 | +0.54 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDLIM5]] | -0.61 | -0.43 / -0.56 | both halves | 3e-05 |  |
| [[DDX5]] | -0.58 | -0.59 / -0.59 | both halves | 7e-06 |  |
| [[TJP1]] | -0.58 | -0.46 / -0.59 | both halves | 2e-05 |  |
| [[PTPRK]] | -0.53 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[RNF32-AS1]] | -0.53 | -0.64 / -0.44 | both halves | 3e-05 |  |
| [[MFSD14CP-1]] | -0.51 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[LINC00342]] | -0.51 | -0.51 / -0.33 | both halves | 1e-04 |  |
| [[PITPNB]] | -0.51 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[DOCK1]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RRAGD]] | B | RRAGD activity raises PMS2CL's level | lines that do not express RRAGD (14) vs lines expressing it (36) | 1.31× lower at baseline in the lines without RRAGD | 0.055 | ⚠ within organs, on part of the lines; also absent: ANKRD6, HDGFL3, RIMKLB |
| [[TOP2A]] | B | TOP2A activity raises PMS2CL's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Mitoxantrone) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[PLEKHA2]] | C | PLEKHA2 activity lowers PMS2CL's level | lines that do not express PLEKHA2 (4) vs lines expressing it (45) | 1.53× higher at baseline in the lines without PLEKHA2 | 0.086 | ⚠ few lines (4 vs 45); within organs, on part of the lines; also absent: LSMEM2, ENSG00000285868; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (9.1, -19.8); signed map (-39.8, 21.4). **Vector** length 59.6, 9.21% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +2.8 | +10.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.6 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.1 | -2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +4.0 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -4.0 |
|  | [[Megestrol (drug)]] 0.05 µM |  | -2.1 | -4.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -2.0 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.3 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.7 | +3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -0.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -1.0 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | -1.7 | -2.4 |
|  | [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | PMS2 C-terminal like (pseudogene) |
| Locus type | pseudogene |
| Location | 7p22.1 — chr7:6,735,305-6,751,392 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | PMS2P13 |
| Matched by | ensembl_id |

UniProt [Q68D20](https://www.uniprot.org/uniprotkb/Q68D20) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:30061](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30061) · Entrez [441194](https://www.ncbi.nlm.nih.gov/gene/441194) · UniProt [Q68D20](https://www.uniprot.org/uniprotkb/Q68D20) · Ensembl [ENSG00000187953](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187953)

## Data

Gene col 11959: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11959); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11959, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11959]; `tensor/DDL_lfc|DDL_z.npy` [11959]; `embed/gene_vectors.npy` [11959]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11959 or target_col == 11959). Every well: [[PMS2CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
