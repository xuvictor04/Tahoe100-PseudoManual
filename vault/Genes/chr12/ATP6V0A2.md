---
symbol: "ATP6V0A2"
type: "gene"
col: 11664
ensembl_id: "ENSG00000185344"
name: "ATPase H+ transporting V0 subunit a2"
location: "12q24.31"
module: 36
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# ATP6V0A2

*ATPase H+ transporting V0 subunit a2* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 3.41× (z +22.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.713× (z -6.4, q 9e-08, down in 26 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATAD3A]] (+0.59, fdr 9e-05), [[TREX2]] (+0.58, fdr 8e-05), [[CTU2]] (+0.56, fdr 6e-05); moves opposite to [[ATP6V1A]] (-0.54, fdr 2e-05), [[MYLIP]] (-0.53, fdr 4e-05), [[DUSP19]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11664.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **3.41×** | +22.9 | 0e+00 | 47/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.19×** | +21.7 | 0e+00 | 48/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.83×** | +19.5 | 0e+00 | 45/47 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +15.7 | 0e+00 | 42/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.77×** | +14.3 | 3e-44 | 37/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +10.8 | 3e-25 | 34/45 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.49×** | +9.8 | 6e-21 | 31/47 (HEC-1-A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.69×** | +9.4 | 5e-19 | 34/48 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.65×** | +9.3 | 8e-19 | 31/48 (SW480, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.61×** | +8.9 | 3e-17 | 36/47 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +7.7 | 6e-13 | 32/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.51×** | +7.7 | 8e-13 | 30/47 (AsPC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +7.2 | 2e-11 | 29/47 (NCI-H460, Hs 766T, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.50×** | +7.2 | 2e-11 | 28/47 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.49×** | +7.1 | 5e-11 | 29/47 (LOX-IMVI, C32, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.41×** | +6.4 | 7e-09 | 27/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.6 | 8e-07 | 22/48 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.34×** | +5.4 | 2e-06 | 22/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.33×** | +5.3 | 4e-06 | 21/47 (SW480, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11664.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.713×** | -6.4 | 9e-08 | 26/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.793×** | -6.0 | 5e-07 | 22/48 (SW480, RPMI-7951, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.807×** | -5.4 | 1e-05 | 24/48 (SW1417, HS-578T, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **0.783×** | -4.6 | 5e-04 | 15/48 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[NG25 (drug)]] 5 µM |  | **0.628×** | -4.6 | 5e-04 | 17/46 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.796×** | -4.3 | 0.001 | 20/48 (HS-578T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Verteporfin (drug)]] 0.05 µM |  | **0.821×** | -3.5 | 0.043 | 14/47 (CHP-212, SW48, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.719×** | -3.3 | 0.063 | 16/48 (A-427, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Busulfan (drug)]] 0.05 µM |  | 0.843× | -3.3 | 0.063 | 10/48 (SW 1088, NCI-H1792, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | 0.843× | -3.3 | 0.063 | 9/48 (PANC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.853× | -3.0 | 0.12 | 9/47 (A-172, AsPC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11664. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.1 | 7 | 1 | [[Panobinostat (drug)]] 0.5 µM 3.87× (z +16.1) | [[Tucidinostat (drug)]] 0.5 µM 0.473× (z -8.9) |
| [[PANC-1 (line)]] | alt | 28.2 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +13.3) | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.74× (z +11.0) | — |
| [[LOX-IMVI (line)]] | wt | 22.2 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.59× (z +11.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.18× (z +10.6) | — |
| [[A-172 (line)]] | wt | 20.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.87× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 25.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.84× (z +11.4) | — |
| [[NCI-H23 (line)]] | alt | 39.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.37× (z +9.4) | — |
| [[NCI-H2347 (line)]] | alt | 19.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +10.0) | — |
| [[NCI-H460 (line)]] | wt | 23.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.04× (z +9.4) | — |
| [[SW1417 (line)]] | alt | 26.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.19× (z +10.0) | — |
| [[A-427 (line)]] | wt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.31× (z +9.2) | — |
| [[A549 (line)]] | wt | 20.9 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.82× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 9.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 25.6 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +9.1) | — |
| [[SHP-77 (line)]] | alt | 65.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +10.7) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 36.7 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.53× (z +9.7) | — |
| [[AN3 CA (line)]] | alt | 38.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0807× (z -9.8) |
| [[COLO 205 (line)]] | alt | 17.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.54× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 14.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.54× (z +8.9) | — |
| [[KATO III (line)]] | alt | 20.8 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.46× (z +8.8) | — |
| [[LoVo (line)]] | wt | 27.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.29× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 15.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 20.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.39× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +8.7) | — |
| [[SNU-423 (line)]] | alt | 14.3 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.35× (z +9.1) | — |
| [[A498 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11664), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATAD3A]] | +0.59 | +0.36 / +0.65 | both halves | 9e-05 |  |
| [[TREX2]] | +0.58 | +0.37 / +0.68 | both halves | 8e-05 |  |
| [[CTU2]] | +0.56 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[MTOR]] | +0.55 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[ATAD3B]] | +0.55 | +0.35 / +0.61 | both halves | 1e-04 |  |
| [[SPOUT1]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[CAMKK2]] | +0.53 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[TMEM181]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[EEFSEC]] | +0.52 | +0.48 / +0.50 | both halves | 2e-05 |  |
| [[SCLY]] | +0.52 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[CNDP2]] | +0.51 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[CCM2]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1A]] | -0.54 | -0.48 / -0.51 | both halves | 2e-05 | same gene group; pathway: Insulin receptor recycling; STRING 986 |
| [[MYLIP]] | -0.53 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[DUSP19]] | -0.53 | -0.40 / -0.46 | both halves | 5e-05 |  |
| [[PUM1]] | -0.52 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[DOC2A]] | -0.51 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PCOLCE]] | -0.51 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ATF2]] | -0.51 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[CTNNB1]] | -0.50 | -0.40 / -0.52 | both halves | 5e-05 |  |
| [[SDAD1P1]] | -0.50 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[BDH2]] | -0.50 | -0.22 / -0.52 | both halves | 6e-04 |  |
| [[ERICH6-AS1]] | -0.50 | -0.41 / -0.39 | both halves | 5e-05 |  |
| [[HMGN5]] | -0.49 | -0.33 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATP6V0A2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.386). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-5.2, -27.6); signed map (-46.2, -17.1). **Vector** length 84.0, 19.3% of its response variance represented; |z| ≥ 3 in 1,135 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | +3.6 | +5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.3 | +15.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.2 | +7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +2.9 | +9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.3 | +3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +3.0 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.7 | +3.1 |
| fall | [[Selinexor (drug)]] 5 µM |  | -7.6 | -5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -7.1 | -6.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -6.9 | -6.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.1 | -3.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.3 | -4.3 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.0 | -2.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.0 | -0.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.6 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V0 subunit a2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:123,712,353-123,761,755 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TJ6, a2, TJ6s, TJ6M, ATP6a2, J6B7, ATP6N1D, Vph1 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Reactome | 9 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y487](https://www.uniprot.org/uniprotkb/Q9Y487) (V-type proton ATPase 116 kDa subunit a 2):

> Subunit of the V0 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons (By similarity). V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment (By similarity). Essential component of the endosomal …

**Summary**, from NCBI Gene [23545](https://www.ncbi.nlm.nih.gov/gene/23545):

> The protein encoded by this gene is a subunit of the vacuolar ATPase (v-ATPase), an heteromultimeric enzyme that is present in intracellular vesicles and in the plasma membrane of specialized cells, and which is essential for the acidification of diverse cellular components. V-ATPase is comprised of a membrane peripheral V(1) domain for ATP hydrolysis, and an integral membrane V(0) domain for proton translocation. The subunit encoded by this gene is a component of the V(0) domain. Mutations in …

**Accessions** — [HGNC:18481](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18481) · Entrez [23545](https://www.ncbi.nlm.nih.gov/gene/23545) · UniProt [Q9Y487](https://www.uniprot.org/uniprotkb/Q9Y487) · Ensembl [ENSG00000185344](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185344)

## Data

Gene col 11664: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11664); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11664, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11664]; `tensor/DDL_lfc|DDL_z.npy` [11664]; `embed/gene_vectors.npy` [11664]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11664 or target_col == 11664). Every well: [[ATP6V0A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V0A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
