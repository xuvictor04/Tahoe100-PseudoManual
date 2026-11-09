---
symbol: "SP2"
type: "gene"
col: 9429
ensembl_id: "ENSG00000167182"
name: "Sp2 transcription factor"
location: "17q21.32"
module: 173
arm: "+"
pooled_cpm: 20.14
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/173"]
generated_by: "tahoemap"
---

# SP2

*Sp2 transcription factor* — 17q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +15.0, q 0e+00, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.685× (z -5.1, q 2e-04, down in 24 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 0.783× (z -4.9, q 2e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIS12]] (+0.73, fdr 7e-06), [[ZNF543]] (+0.72, fdr 8e-06), [[NAIF1]] (+0.72, fdr 1e-05); moves opposite to [[METAP1]] (-0.70, fdr 1e-05), [[STX7]] (-0.68, fdr 1e-05), [[ATP5F1C]] (-0.66, fdr 1e-05).
> It is in [[Module 173]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9429.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +15.0 | 0e+00 | 42/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.08×** | +9.9 | 1e-20 | 41/47 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +9.2 | 5e-18 | 35/47 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +6.5 | 2e-08 | 29/47 (NCI-H460, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.39×** | +6.4 | 2e-08 | 27/45 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.34×** | +6.2 | 4e-08 | 32/48 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.37×** | +4.4 | 9e-04 | 23/47 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9429.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.685×** | -5.1 | 2e-04 | 24/47 (BT-474, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.703×** | -4.9 | 2e-04 | 25/42 (SHP-77, SK-MEL-2, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.783×** | -4.9 | 2e-04 | 25/48 (A-427, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.736×** | -4.3 | 0.002 | 22/48 (NCI-H1792, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.723×** | -4.2 | 0.003 | 16/37 (SNU-423, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.751×** | -4.0 | 0.005 | 16/47 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.758×** | -3.9 | 0.007 | 17/48 (NCI-H1792, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.822×** | -3.9 | 0.007 | 22/48 (A-427, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.761×** | -3.8 | 0.008 | 18/47 (NCI-H1792, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.768×** | -3.7 | 0.011 | 17/47 (SW48, COLO 205, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Radotinib (drug)]] 5 µM |  | 0.856× | -3.1 | 0.10 | 11/48 (Panc 03.27, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9429. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +16.6) | — |
| [[A-427 (line)]] | wt | 24.1 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.347× (z -9.7) |
| [[A549 (line)]] | wt | 19.0 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +14.0) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H1573 (line)]] | alt | 16.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.83× (z +10.3) | — |
| [[RKO (line)]] | wt | 20.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +11.2) | — |
| [[SHP-77 (line)]] | alt | 22.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SK-MEL-2 (line)]] | alt | 27.6 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.07× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A-172 (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0923× (z -13.1) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A498 (line)]] | wt | 12.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 13.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +8.7) | — |
| [[BT-474 (line)]] | alt | 16.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.149× (z -9.6) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.67× (z +9.1) | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 1 | — | [[PH-797804 (drug)]] 0.5 µM 0.0904× (z -8.5) |
| [[HepG2_C3A (line)]] | wt | 19.0 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.116× (z -10.1) |
| [[HOP62 (line)]] | alt | 20.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.0) | — |
| [[LoVo (line)]] | wt | 21.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.6) | — |
| [[NCI-H2030 (line)]] | alt | 14.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.77× (z +14.8) | — |
| [[NCI-H23 (line)]] | alt | 25.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 19.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +8.9) | — |
| [[PANC-1 (line)]] | alt | 27.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +11.2) | — |
| [[SNU-1 (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 22.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0724× (z -15.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 25.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 18.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9429), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIS12]] | +0.73 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[ZNF543]] | +0.72 | +0.68 / +0.58 | both halves | 8e-06 | same gene group |
| [[NAIF1]] | +0.72 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[SCAF1]] | +0.71 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[FIZ1]] | +0.71 | +0.69 / +0.60 | both halves | 7e-06 | same gene group |
| [[INO80D]] | +0.71 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[COQ7]] | +0.70 | +0.68 / +0.58 | both halves | 8e-06 |  |
| [[USP11]] | +0.69 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[ZNF646]] | +0.69 | +0.75 / +0.51 | both halves | 1e-05 | same gene group |
| [[ZNF689]] | +0.69 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[ZC3H4]] | +0.68 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[TSTD2]] | +0.68 | +0.57 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[METAP1]] | -0.70 | -0.72 / -0.55 | both halves | 1e-05 |  |
| [[STX7]] | -0.68 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[ATP5F1C]] | -0.66 | -0.57 / -0.58 | both halves | 1e-05 |  |
| [[HACE1]] | -0.65 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[RNF149]] | -0.64 | -0.68 / -0.55 | both halves | 1e-05 |  |
| [[TMEM185A]] | -0.64 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[HEBP1]] | -0.64 | -0.64 / -0.45 | both halves | 3e-05 |  |
| [[STAM]] | -0.64 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[SERAC1]] | -0.63 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[LTA4H]] | -0.62 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[USP3]] | -0.62 | -0.73 / -0.47 | both halves | 2e-05 |  |
| [[ELP2]] | -0.62 | -0.59 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises SP2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises SP2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF888]] | B | ZNF888 activity raises SP2's level | lines that do not express ZNF888 (6) vs lines expressing it (44) | 1.19× lower at baseline in the lines without ZNF888 | 0.098 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ZNF816, ZNF468, ZNF701 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 173]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.728). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-8.5, 6.1); signed map (14.5, -22.9). **Vector** length 95.8, 20.9% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.6 | +15.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +9.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.2 | +6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.1 | +2.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +6.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +1.3 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -4.7 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -3.8 | -3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -3.7 | -3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.5 | -1.0 |
|  | [[Terfenadine (drug)]] 5 µM |  | -2.2 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.0 | -3.1 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.9 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | Sp2 transcription factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.32 — chr17:47,896,150-47,928,957 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0048 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Sp transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02086](https://www.uniprot.org/uniprotkb/Q02086) (Transcription factor Sp2):

> Binds to GC box promoters elements and selectively activates mRNA synthesis from genes that contain functional recognition sites.

**Summary**, from NCBI Gene [6668](https://www.ncbi.nlm.nih.gov/gene/6668):

> This gene encodes a member of the Sp subfamily of Sp/XKLF transcription factors. Sp family proteins are sequence-specific DNA-binding proteins characterized by an amino-terminal trans-activation domain and three carboxy-terminal zinc finger motifs. This protein contains the least conserved DNA-binding domain within the Sp subfamily of proteins, and its DNA sequence specificity differs from the other Sp proteins. It localizes primarily within subnuclear foci associated with the nuclear matrix, …

**Accessions** — [HGNC:11207](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11207) · Entrez [6668](https://www.ncbi.nlm.nih.gov/gene/6668) · UniProt [Q02086](https://www.uniprot.org/uniprotkb/Q02086) · Ensembl [ENSG00000167182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167182)

## Data

Gene col 9429: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9429); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9429, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9429]; `tensor/DDL_lfc|DDL_z.npy` [9429]; `embed/gene_vectors.npy` [9429]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9429 or target_col == 9429). Every well: [[SP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
