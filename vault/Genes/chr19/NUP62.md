---
symbol: "NUP62"
type: "gene"
col: 13076
ensembl_id: "ENSG00000213024"
name: "nucleoporin 62"
location: "19q13.33"
module: 16
arm: "+"
pooled_cpm: 22.96
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# NUP62

*nucleoporin 62* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +13.2, q 4e-37, up in 31 of 47 measured lines) ⚠ cell-cycle shift, explains ~39% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 1.62× (z +7.1, q 2e-10, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.735× (z -4.5, q 0.004, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR82]] (+0.73, fdr 7e-06), [[TRIM47]] (+0.65, fdr 7e-06), [[IL4I1]] (+0.62, fdr 1e-05, ⚠ same locus), [[ZNF24]] (+0.62, fdr 1e-05); moves opposite to [[BTAF1]] (-0.65, fdr 1e-05), [[AP3S1]] (-0.60, fdr 1e-05), [[STRAP]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13076.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.89×** | +13.2 | 4e-37 | 31/47 (J82, A498, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.81×** | +8.4 | 2e-14 | 30/48 (J82, PANC-1, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **1.66×** | +7.4 | 2e-11 | 34/45 (NCI-H2030, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.62×** | +7.1 | 2e-10 | 30/47 (HS-578T, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.54×** | +6.0 | 2e-07 | 30/48 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.43×** | +5.2 | 2e-05 | 25/47 (A-427, C-33 A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +4.7 | 2e-04 | 21/48 (NCI-H2347, HOP62, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.7 | 2e-04 | 20/44 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.32×** | +4.0 | 0.003 | 16/47 (PANC-1, SW1417, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.31×** | +4.0 | 0.004 | 18/47 (PANC-1, HS-578T, …) | two highest doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.30×** | +3.9 | 0.006 | 13/48 (A498, A-172, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.013 | 12/46 (LS 180, SW48, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.5 | 0.017 | 16/47 (J82, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.27×** | +3.4 | 0.026 | 17/46 (NCI-H2347, H4, …) | top dose only | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.26×** | +3.3 | 0.031 | 16/47 (KATO III, PANC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.032 | 12/47 (NCI-H2030, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.52×** | +3.2 | 0.043 | 7/46 (MIA PaCa-2, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.16× | +3.1 | 0.049 | 12/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **1.25×** | +3.1 | 0.049 | 11/46 (J82, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.064 | 6/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13076.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.735×** | -4.5 | 0.004 | 23/47 (SNU-423, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.760×** | -4.0 | 0.017 | 22/48 (A498, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.923× | -3.9 | 0.017 | 3/48 (hTERT-HPNE, CHP-212, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.761×** | -3.8 | 0.019 | 21/47 (SW 900, A549, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.846× | -3.5 | 0.063 | 18/48 (Panc 03.27, SW 900, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.854× | -3.3 | 0.10 | 14/48 (HOP62, SW 1088, …) | rises with dose | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | 0.808× | -3.1 | 0.14 | 7/47 (J82, HT-29, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13076. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 49.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +13.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 3.02× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 19.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +11.5) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.79× (z +8.9) | — |
| [[A-172 (line)]] | wt | 38.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.1) ⚠ cell-cycle shift, explains ~39% of this change | [[Dinaciclib (drug)]] 5 µM 0.296× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 22.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.04× (z +9.7) | — |
| [[J82 (line)]] | alt | 32.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.40× (z +17.6) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[A-427 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 24.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +10.0) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[CFPAC-1 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +8.9) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LoVo (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.90× (z +10.4) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1792 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +11.0) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 24.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.267× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 18.6 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.166× (z -11.5) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.281× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 23.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13076), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR82]] | +0.73 | +0.64 / +0.74 | both halves | 7e-06 |  |
| [[TRIM47]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[IL4I1]] | +0.62 | +0.66 / +0.54 | both halves | 1e-05 | STRING 868; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF24]] | +0.62 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[GTF3C4]] | +0.62 | +0.57 / +0.65 | both halves | 8e-06 |  |
| [[UBQLN2]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[NOL11]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[RTL6]] | +0.61 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[METTL18]] | +0.60 | +0.61 / +0.56 | both halves | 1e-05 |  |
| [[THUMPD1]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ZNF689]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[JAGN1]] | +0.59 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[ZNF155]] | +0.59 | +0.54 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTAF1]] | -0.65 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[AP3S1]] | -0.60 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[STRAP]] | -0.58 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[SNX1]] | -0.55 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.54 | -0.63 / -0.42 | both halves | 4e-05 | pathway: HCMV Early Events |
| [[PPP1R2]] | -0.54 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[TMEM50B]] | -0.54 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[QSOX1]] | -0.54 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[RPL41]] | -0.53 | -0.50 / -0.60 | both halves | 1e-05 | pathway: Influenza Infection |
| [[PMS2P3-1]] | -0.53 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[NPDC1]] | -0.53 | -0.51 / -0.39 | both halves | 5e-05 |  |
| [[RAP1A]] | -0.53 | -0.60 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity raises NUP62's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[HYLS1]] | B | HYLS1 activity raises NUP62's level | lines that do not express HYLS1 (5) vs lines expressing it (45) | 1.30× lower at baseline in the lines without HYLS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DNAJB5, PPP2R3A, CEP170; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.533). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-37.0, 12.5); signed map (2.4, -24.2). **Vector** length 94.7, 22.0% of its response variance represented; |z| ≥ 3 in 705 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +7.0 | +8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +6.8 | +13.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +7.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.5 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +3.2 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +1.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +2.1 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +2.4 |
|  | [[Thymol (drug)]] 5 µM |  | +2.2 | +3.1 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.8 | -2.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.6 | -0.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.8 | +0.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Glycyrrhizic acid (drug)]] 0.5 µM |  | -2.0 | -3.8 |
|  | [[Dihydroartemisinin (drug)]] 5 µM |  | -1.9 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.7 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | nucleoporin 62 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,906,825-49,929,764 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p62, DKFZp547L134, IBSN, SNDI, MGC841, FLJ20822, FLJ43869 |
| Gene groups (HGNC) | Nucleoporins |
| Reactome | 73 pathways, smallest: Postmitotic nuclear pore complex (NPC) reformation; IP3 and IP4 transport between cytosol and nucleus; IP6 and IP7 transport between cytosol and nucleus |
| Matched by | ensembl_id |

**Function**, from UniProt [P37198](https://www.uniprot.org/uniprotkb/P37198) (Nuclear pore glycoprotein p62):

> Essential component of the nuclear pore complex. The N-terminal is probably involved in nucleocytoplasmic transport. The C-terminal is involved in protein-protein interaction probably via coiled-coil formation, promotes its association with centrosomes and may function in anchorage of p62 to the pore complex. Plays a role in mitotic cell cycle progression by regulating centrosome segregation, centriole maturation and spindle orientation. It might be involved in protein recruitment to the …

**Summary**, from NCBI Gene [23636](https://www.ncbi.nlm.nih.gov/gene/23636):

> The nuclear pore complex is a massive structure that extends across the nuclear envelope, forming a gateway that regulates the flow of macromolecules between the nucleus and the cytoplasm. Nucleoporins are the main components of the nuclear pore complex in eukaryotic cells. The protein encoded by this gene is a member of the FG-repeat containing nucleoporins and is localized to the nuclear pore central plug. This protein associates with the importin alpha/beta complex which is involved in the …

**Accessions** — [HGNC:8066](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8066) · Entrez [23636](https://www.ncbi.nlm.nih.gov/gene/23636) · UniProt [P37198](https://www.uniprot.org/uniprotkb/P37198) · Ensembl [ENSG00000213024](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213024)

## Data

Gene col 13076: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13076); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13076, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13076]; `tensor/DDL_lfc|DDL_z.npy` [13076]; `embed/gene_vectors.npy` [13076]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13076 or target_col == 13076). Every well: [[NUP62 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUP62.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
