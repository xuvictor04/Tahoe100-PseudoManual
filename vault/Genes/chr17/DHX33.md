---
symbol: "DHX33"
type: "gene"
col: 67
ensembl_id: "ENSG00000005100"
name: "DEAH-box helicase 33"
location: "17p13.2"
module: 5
arm: "+"
pooled_cpm: 24.55
n_lines_expressing: 50
n_dd_up: 39
n_dd_down: 7
n_dd_up_clean: 25
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# DHX33

*DEAH-box helicase 33* — 17p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 39 drug-doses (14 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 2.01× (z +15.2, q 0e+00, up in 45 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +9.7, q 3e-20, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.678× (z -12.0, q 1e-30, down in 27 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOP16]] (+0.80, fdr 7e-06), [[URB2]] (+0.80, fdr 7e-06), [[MDN1]] (+0.78, fdr 7e-06); moves opposite to [[SKAP2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LTBR]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 71 in all, 27 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 39 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 67.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.01×** | +15.2 | 0e+00 | 45/47 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.77×** | +12.0 | 8e-31 | 37/46 (A-172, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **1.73×** | +11.0 | 7e-26 | 27/42 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.42×** | +10.8 | 8e-25 | 31/48 (A549, A-172, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +9.7 | 3e-20 | 31/47 (C-33 A, AN3 CA, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +9.3 | 1e-18 | 27/47 (J82, A-172, …) | two highest doses | cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.55×** | +9.2 | 2e-18 | 31/46 (J82, NCI-H1792, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.52×** | +8.7 | 2e-16 | 33/47 (NCI-H1792, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.09×** | +8.4 | 3e-15 | 31/46 (NCI-H460, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.46×** | +8.2 | 1e-14 | 26/48 (SW480, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.00×** | +7.9 | 1e-13 | 26/46 (PANC-1, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.92×** | +7.5 | 4e-12 | 12/27 (NCI-H2030, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.89×** | +7.2 | 2e-11 | 27/47 (NCI-H460, A498, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.38×** | +7.1 | 6e-11 | 21/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.84×** | +6.9 | 2e-10 | 22/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +6.2 | 2e-08 | 17/48 (A-172, HOP62, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.70×** | +6.0 | 5e-08 | 23/48 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.64×** | +5.6 | 5e-07 | 17/46 (A498, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +5.6 | 5e-07 | 15/46 (A498, A549, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +5.4 | 2e-06 | 16/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.26×** | +5.1 | 7e-06 | 13/47 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +4.8 | 4e-05 | 13/46 (NCI-H460, NCI-H23, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 67.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.678×** | -12.0 | 1e-30 | 27/47 (RKO, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.822×** | -6.1 | 3e-07 | 19/48 (A498, SW1417, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.801×** | -4.9 | 2e-04 | 16/47 (NCI-H2030, A498, …) | two highest doses | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.809×** | -4.6 | 5e-04 | 20/47 (HS-578T, COLO 205, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.819×** | -4.2 | 0.003 | 19/47 (hTERT-HPNE, SW48, …) | two highest doses |  |
| [[Rifaximin (drug)]] 5 µM |  | **0.820×** | -4.2 | 0.003 | 7/47 (RKO, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Rifaximin (drug)]] 0.5 µM |  | **0.831×** | -4.1 | 0.004 | 8/47 (J82, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Pimitespib (drug)]] 0.05 µM |  | 0.840× | -3.6 | 0.020 | 7/48 (NCI-H23, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 0.895× | -3.5 | 0.035 | 9/48 (HEC-1-A, Hs 766T, …) | top dose only |  |
| [[Verteporfin (drug)]] 5 µM |  | 0.862× | -3.2 | 0.090 | 10/47 (C-33 A, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.38 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 67. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 29.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.05 µM 3.23× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.7) |
| [[RKO (line)]] | wt | 60.1 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -25.6) |
| [[NCI-H23 (line)]] | alt | 51.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.165× (z -17.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.444× (z -11.4) |
| [[NCI-H661 (line)]] | alt | 35.2 | 0 | 2 | — | [[Naproxen (drug)]] 5 µM 0.0541× (z -9.5) |
| [[A-172 (line)]] | wt | 19.6 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.70× (z +10.7) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 36.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -15.6) |
| [[A498 (line)]] | wt | 28.2 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.51× (z +9.9) ⚠ unreliable plate only | — |
| [[A549 (line)]] | wt | 25.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +10.8) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[C-33 A (line)]] | alt | 51.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.419× (z -9.5) |
| [[C32 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 4.28× (z +8.6) ⚠ unreliable plate only | — |
| [[PANC-1 (line)]] | alt | 33.4 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.10× (z +9.4) ⚠ unreliable plate only | — |
| [[SHP-77 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~96% of this change |
| [[SNU-1 (line)]] | wt | 33.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -8.5) |
| [[SW48 (line)]] | wt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -8.9) |
| [[SW480 (line)]] | alt | 46.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.546× (z -9.7) |
| [[AN3 CA (line)]] | alt | 37.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 67), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOP16]] | +0.80 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[URB2]] | +0.80 | +0.84 / +0.82 | both halves | 7e-06 |  |
| [[MDN1]] | +0.78 | +0.85 / +0.77 | both halves | 7e-06 |  |
| [[WDR4]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.76 | +0.77 / +0.82 | both halves | 7e-06 |  |
| [[TWNK]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 |  |
| [[WDR3]] | +0.76 | +0.75 / +0.84 | both halves | 7e-06 | STRING 520 |
| [[UCK2]] | +0.74 | +0.79 / +0.70 | both halves | 7e-06 |  |
| [[NOP2]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[PA2G4]] | +0.74 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[DDX31]] | +0.74 | +0.67 / +0.79 | both halves | 7e-06 |  |
| [[URB1]] | +0.74 | +0.78 / +0.72 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SKAP2]] | -0.62 | -0.55 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LTBR]] | B | LTBR activity lowers DHX33's level | lines that do not express LTBR (8) vs lines expressing it (42) | 1.62× higher at baseline in the lines without LTBR | 0.039 | ⚠ within organs, on part of the lines; also absent: SIGIRR, YPEL3, CLCF1 |
| [[PDE3B]] | B | PDE3B activity raises DHX33's level | lines that do not express PDE3B (20) vs lines expressing it (30) | 1.45× lower at baseline in the lines without PDE3B | 0.074 | ⚠ within organs, on part of the lines; also absent: ENSG00000250049, MIR4458HG, ASB4 |
| [[GALNT14]] | B | GALNT14 activity lowers DHX33's level | lines that do not express GALNT14 (24) vs lines expressing it (26) | 1.29× higher at baseline in the lines without GALNT14 | 0.075 | ⚠ within organs, on part of the lines; also absent: NOVA1, SLC35F3, ZYG11A |
| [[TOP2A]] | B | TOP2A activity lowers DHX33's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.1% of all compounds | 0.075 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ALDH1B1]] | C | ALDH1B1 activity raises DHX33's level | lines that do not express ALDH1B1 (3) vs lines expressing it (47) | 2.38× lower at baseline in the lines without ALDH1B1 | 0.085 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CENPP, CDC25A, NDC80; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.792). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.1, -37.5); signed map (-4.1, -49.7). **Vector** length 101, 24.0% of its response variance represented; |z| ≥ 3 in 1,043 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.65 to 13); *rRNA processing* (reactome, mean cos +0.59 to 20); *rRNA processing in the nucleus and cytosol* (reactome, mean cos +0.58 to 19).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.5 | +15.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.5 | +12.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.8 | +7.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | +4.5 | +9.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.4 | +7.2 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.4 | +8.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +6.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.5 | -12.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -6.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.2 | -4.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | -3.1 | +2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.1 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.1 | -4.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.0 | -0.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.8 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | DEAH-box helicase 33 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.2 — chr17:5,440,917-5,468,982 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21972, DKFZp762F2011; previously DDX33 |
| Gene groups (HGNC) | DEAH-box helicases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6R0](https://www.uniprot.org/uniprotkb/Q9H6R0) (ATP-dependent RNA helicase DHX33):

> Implicated in nucleolar organization, ribosome biogenesis, protein synthesis and cytoplasmic dsRNA sensing (By similarity). Stimulates RNA polymerase I transcription of the 47S precursor rRNA. Associates with ribosomal DNA (rDNA) loci where it is involved in POLR1A recruitment. In the cytoplasm, promotes elongation-competent 80S ribosome assembly at the late stage of mRNA translation initiation. Senses cytosolic dsRNA mediating NLRP3 inflammasome formation in macrophages and type I interferon …

**Summary**, from NCBI Gene [56919](https://www.ncbi.nlm.nih.gov/gene/56919):

> This gene encodes a member of the DEAD box protein family. The DEAD box proteins are characterized by the conserved motif Asp-Glu-Ala-Asp (DEAD), are putative RNA helicases. They are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Based on their distribution patterns, some members of this DEAD box protein family are believed to be involved in …

**Accessions** — [HGNC:16718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16718) · Entrez [56919](https://www.ncbi.nlm.nih.gov/gene/56919) · UniProt [Q9H6R0](https://www.uniprot.org/uniprotkb/Q9H6R0) · Ensembl [ENSG00000005100](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005100)

## Data

Gene col 67: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 67); `tables/drug_effects.parquet` (81 rows, flagged included); `relations/gene_relations.parquet` (col_a == 67, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 67]; `tensor/DDL_lfc|DDL_z.npy` [67]; `embed/gene_vectors.npy` [67]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 67 or target_col == 67). Every well: [[DHX33 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHX33.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
