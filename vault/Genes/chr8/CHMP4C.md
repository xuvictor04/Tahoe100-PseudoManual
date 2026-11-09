---
symbol: "CHMP4C"
type: "gene"
col: 8992
ensembl_id: "ENSG00000164695"
name: "charged multivesicular body protein 4C"
location: "8q21.13"
module: 20
arm: "-"
pooled_cpm: 33.17
n_lines_expressing: 34
n_dd_up: 4
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CHMP4C

*charged multivesicular body protein 4C* — 8q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 1.23× (z +4.6, q 0.002, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.446× (z -13.0, q 7e-36, down in 29 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADPRM]] (+0.56, fdr 3e-05), [[GADD45A]] (+0.55, fdr 3e-05), [[GATAD1]] (+0.52, fdr 1e-04); moves opposite to [[USP5]] (-0.52, fdr 3e-05), [[POLR2E]] (-0.49, fdr 1e-04), [[EIF5A]] (-0.49, fdr 3e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 5 go from it, the strongest it → [[MAPK13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8992.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +4.6 | 0.002 | 17/33 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.037 | 16/32 (A-427, NCI-H1573, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.25×** | +3.6 | 0.050 | 12/31 (BT-474, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.24×** | +3.4 | 0.092 | 14/32 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | 1.15× | +3.2 | 0.12 | 11/32 (RKO, HEC-1-A, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.22× | +3.2 | 0.12 | 14/31 (AsPC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.22× | +3.2 | 0.12 | 11/31 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | 1.30× | +3.0 | 0.17 | 11/31 (HCT15, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8992.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.446×** | -13.0 | 7e-36 | 29/32 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.479×** | -11.9 | 5e-30 | 28/32 (RKO, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.552×** | -9.6 | 2e-19 | 30/32 (RKO, KATO III, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.608×** | -8.0 | 2e-13 | 23/31 (RKO, A549, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.610×** | -7.9 | 2e-13 | 21/32 (RKO, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.549×** | -5.0 | 4e-05 | 19/33 (KATO III, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.837× | -3.9 | 0.006 | 14/32 (NCI-H1573, AsPC-1, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.794×** | -3.7 | 0.015 | 14/32 (Panc 03.27, AsPC-1, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.795×** | -3.7 | 0.015 | 11/32 (KATO III, CFPAC-1, …) | inconsistent across doses |  |
| [[Arbutin (drug)]] 0.5 µM |  | **0.798×** | -3.6 | 0.016 | 15/32 (J82, HOP62, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.05 µM |  | **0.807×** | -3.4 | 0.027 | 13/32 (SW480, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.824×** | -3.4 | 0.027 | 17/33 (AsPC-1, RKO, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.801×** | -3.4 | 0.027 | 11/31 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.861× | -3.4 | 0.027 | 15/32 (HT-29, SW480, …) | top dose only | composition shift |
| [[RMC-6236 (drug)]] 5 µM |  | **0.670×** | -3.4 | 0.029 | 9/32 (HEC-1-A, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.813×** | -3.3 | 0.030 | 15/33 (NCI-H1573, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8992. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 47.3 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.352× (z -12.1) |
| [[HT-29 (line)]] | alt | 98.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.287× (z -13.8) |
| [[KATO III (line)]] | alt | 84.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.286× (z -12.9) |
| [[CFPAC-1 (line)]] | alt | 50.2 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.275× (z -10.6) |
| [[HepG2_C3A (line)]] | wt | 49.4 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.298× (z -9.3) |
| [[LoVo (line)]] | wt | 51.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.219× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 51.0 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.90× (z +10.1) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2347 (line)]] | alt | 74.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.357× (z -12.4) |
| [[RKO (line)]] | wt | 89.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.161× (z -17.6) |
| [[AsPC-1 (line)]] | alt | 48.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.90× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | [[Lonafarnib (drug)]] 5 µM 0.0931× (z -11.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 37.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -9.0) |
| [[HCT15 (line)]] | alt | 51.6 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.186× (z -12.2) |
| [[HEC-1-A (line)]] | alt | 46.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.307× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 17.3 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.135× (z -11.5) |
| [[SW1417 (line)]] | alt | 44.0 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.1) |
| [[A-427 (line)]] | wt | 46.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.126× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A498 (line)]] | wt | 31.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.03× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 28.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +8.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 59.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.370× (z -9.2) |
| [[NCI-H1573 (line)]] | alt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.136× (z -18.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 48.8 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.372× (z -9.0) |
| [[A-172 (line)]] | wt | 2.99 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.04 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.53 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.60 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.83 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.77 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8992), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADPRM]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[GADD45A]] | +0.55 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[GATAD1]] | +0.52 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[EIF3J-DT]] | +0.51 | +0.33 / +0.56 | both halves | 1e-04 |  |
| [[FAM98C]] | +0.51 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[ZNF330]] | +0.51 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[DHRS7]] | +0.50 | +0.30 / +0.58 | both halves | 2e-04 |  |
| [[NRBF2]] | +0.50 | +0.41 / +0.55 | both halves | 4e-05 |  |
| [[KLHL28]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[PYROXD1]] | +0.49 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[ZKSCAN1]] | +0.49 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[SOS2]] | +0.48 | +0.34 / +0.48 | both halves | 1e-04 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP5]] | -0.52 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[POLR2E]] | -0.49 | -0.34 / -0.43 | both halves | 1e-04 | pathway: HIV Infection |
| [[EIF5A]] | -0.49 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[AIFM1]] | -0.48 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[LHPP]] | -0.47 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[BANF1]] | -0.47 | -0.36 / -0.48 | both halves | 9e-05 | pathway: HIV Infection |
| [[PCNX3]] | -0.46 | -0.36 / -0.45 | both halves | 1e-04 |  |
| [[GALNT2]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[TBCD]] | -0.46 | -0.31 / -0.43 | both halves | 2e-04 |  |
| [[MATCAP1]] | -0.45 | -0.24 / -0.43 | both halves | 4e-04 |  |
| [[TUBB]] | -0.45 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[G6PD]] | -0.45 | -0.35 / -0.43 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises CHMP4C's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MAPK13]] | B | MAPK13 activity raises CHMP4C's level | lines that do not express MAPK13 (15) vs lines expressing it (35) | 3.77× lower at baseline in the lines without MAPK13 | 0.073 | ⚠ within organs, on part of the lines; also absent: SPINT1, ENSG00000284644, MCTP2; maybe low, not absent |
| [[ARHGEF5]] | C | ARHGEF5 activity raises CHMP4C's level | lines that do not express ARHGEF5 (19) vs lines expressing it (31) | 6.10× lower at baseline in the lines without ARHGEF5 | 3e-04 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK13]] | B | CHMP4C activity raises MAPK13's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 3.35× lower at baseline in the lines without CHMP4C | 0.063 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[TMEM265]] | B | CHMP4C activity raises TMEM265's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CHMP4C | 0.069 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[WHAMM]] | B | CHMP4C activity raises WHAMM's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without CHMP4C | 0.074 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[ATAD3A]] | B | CHMP4C activity lowers ATAD3A's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 1.14× higher at baseline in the lines without CHMP4C | 0.099 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1 |
| [[ARHGEF5]] | C | CHMP4C activity raises ARHGEF5's level | lines that do not express CHMP4C (16) vs lines expressing it (34) | 4.34× lower at baseline in the lines without CHMP4C | 0.009 | ⚠ within organs, on part of the lines; also absent: TSTD1, BTC, TNK1; co-absent with the target |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.389). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-38.2, -31.7); signed map (-4.7, -0.6). **Vector** length 89.7, 25.9% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +1.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.5 | +2.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.6 | -0.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | -0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.3 | +3.8 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.6 | -2.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.3 | -8.0 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -2.6 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -3.7 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.6 | -2.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -3.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | charged multivesicular body protein 4C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q21.13 — chr8:81,732,448-81,759,515 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC22825, Shax3, VPS32C |
| Gene groups (HGNC) | Charged multivesicular body proteins; ESCRT-III |
| Reactome | 29 pathways, smallest: Translation of Replicase and Assembly of the Replication Transcription Complex_9679504; Translation of Replicase and Assembly of the Replication Transcription Complex_9694676; Pyroptosis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CF2](https://www.uniprot.org/uniprotkb/Q96CF2) (Charged multivesicular body protein 4c):

> Probable core component of the endosomal sorting required for transport complex III (ESCRT-III) which is involved in multivesicular bodies (MVBs) formation and sorting of endosomal cargo proteins into MVBs. MVBs contain intraluminal vesicles (ILVs) that are generated by invagination and scission from the limiting membrane of the endosome and mostly are delivered to lysosomes enabling degradation of membrane proteins, such as stimulated growth factor receptors, lysosomal enzymes and lipids. The …

**Summary**, from NCBI Gene [92421](https://www.ncbi.nlm.nih.gov/gene/92421):

> CHMP4C belongs to the chromatin-modifying protein/charged multivesicular body protein (CHMP) family. These proteins are components of ESCRT-III (endosomal sorting complex required for transport III), a complex involved in degradation of surface receptor proteins and formation of endocytic multivesicular bodies (MVBs). Some CHMPs have both nuclear and cytoplasmic/vesicular distributions, and one such CHMP, CHMP1A (MIM 164010), is required for both MVB formation and regulation of cell cycle …

**Accessions** — [HGNC:30599](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30599) · Entrez [92421](https://www.ncbi.nlm.nih.gov/gene/92421) · UniProt [Q96CF2](https://www.uniprot.org/uniprotkb/Q96CF2) · Ensembl [ENSG00000164695](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164695)

## Data

Gene col 8992: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8992); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8992, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8992]; `tensor/DDL_lfc|DDL_z.npy` [8992]; `embed/gene_vectors.npy` [8992]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8992 or target_col == 8992). Every well: [[CHMP4C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHMP4C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
