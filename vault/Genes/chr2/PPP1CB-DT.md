---
symbol: "PPP1CB-DT"
type: "gene"
col: 13557
ensembl_id: "ENSG00000226833"
name: "PPP1CB divergent transcript"
location: "2p23.2"
module: 15
arm: "+"
pooled_cpm: 5.75
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 20
n_dd_up_clean: 11
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PPP1CB-DT

*PPP1CB divergent transcript* — 2p23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.37× (z +17.5, q 0e+00, up in 32 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.284× (z -12.8, q 2e-34, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NUDT13]] (+0.65, fdr 1e-05), [[H3-3A-DT]] (+0.63, fdr 1e-05), [[CDNF]] (+0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TRPM2-AS]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +17.5 | 0e+00 | 32/36 (LoVo, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.93×** | +6.4 | 3e-08 | 9/22 (HT-29, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.86×** | +6.3 | 5e-08 | 20/46 (KATO III, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.83×** | +5.7 | 2e-06 | 4/15 (CFPAC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +5.3 | 1e-05 | 2/9 (CFPAC-1, A498) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +5.3 | 1e-05 | 17/46 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.003 | 9/42 (NCI-H1573, A549, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +3.8 | 0.010 | 9/40 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.45×** | +3.8 | 0.011 | 7/46 (KATO III, NCI-H2347, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.024 | 5/45 (SW480, HT-29, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.24×** | +3.1 | 0.083 | 5/45 (AsPC-1, LoVo, …) | top dose only | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.083 | 7/46 (A-172, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.35×** | +3.1 | 0.083 | 15/42 (KATO III, SW480, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.35×** | +3.1 | 0.083 | 6/47 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.24×** | +3.1 | 0.084 | 9/44 (HEC-1-A, SW480, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13557.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.284×** | -12.8 | 2e-34 | 33/47 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.324×** | -11.4 | 9e-28 | 27/36 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.405×** | -8.8 | 2e-16 | 25/41 (NCI-H1573, HEC-1-A, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.422×** | -8.8 | 3e-16 | 29/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.450×** | -8.1 | 6e-14 | 27/43 (PANC-1, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.557×** | -5.9 | 3e-07 | 17/35 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~85% of this change | **0.679×** | -5.5 | 2e-06 | 19/38 (HEC-1-A, PANC-1, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.591×** | -5.3 | 7e-06 | 15/46 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.622×** | -4.8 | 1e-04 | 18/45 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.417×** | -4.6 | 2e-04 | 16/39 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~24% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.455×** | -4.2 | 0.002 | 14/33 (HEC-1-A, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.686×** | -3.8 | 0.007 | 11/36 (MIA PaCa-2, C-33 A, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.691×** | -3.7 | 0.008 | 12/42 (PANC-1, SNU-423, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.772×** | -3.7 | 0.009 | 12/44 (HT-29, PANC-1, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.701×** | -3.6 | 0.012 | 15/46 (NCI-H460, HT-29, …) | inconsistent across doses |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | **0.708×** | -3.5 | 0.017 | 6/45 (SW 1271, LS 180, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.715×** | -3.4 | 0.023 | 15/42 (PANC-1, SNU-423, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.737×** | -3.1 | 0.061 | 5/47 (SW1417, PANC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.570×** | -3.0 | 0.083 | 5/37 (A498, HT-29, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 9.35 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.7) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0779× (z -14.7) |
| [[HEC-1-A (line)]] | alt | 32.2 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -19.3) ⚠ cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -12.8) |
| [[NCI-H1573 (line)]] | alt | 16.7 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -12.0) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.143× (z -10.7) |
| [[SW480 (line)]] | alt | 8.65 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0735× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.146× (z -11.1) |
| [[KATO III (line)]] | alt | 11.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0206× (z -16.9) |
| [[NCI-H460 (line)]] | wt | 3.80 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.129× (z -9.0) ⚠ cell-cycle shift, explains ~43% of this change |
| [[A-427 (line)]] | wt | 8.92 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.128× (z -9.8) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 4.80 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0634× (z -9.7) |
| [[HT-29 (line)]] | alt | 9.61 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -9.8) ⚠ cell-cycle shift, explains ~85% of this change |
| [[LoVo (line)]] | wt | 2.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.85× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 3.25 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0597× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 2.34 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.5 µM 0.0678× (z -9.3) |
| [[SNU-423 (line)]] | alt | 4.26 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0951× (z -10.9) ⚠ cell-cycle shift, explains ~85% of this change |
| [[A-172 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.56 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.88 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.06 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.93 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.30 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.10 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT13]] | +0.65 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[H3-3A-DT]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 | same gene group |
| [[CDNF]] | +0.62 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[DMXL1-DT]] | +0.62 | +0.62 / +0.54 | both halves | 1e-05 | same gene group |
| [[HLA-DMA]] | +0.62 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[SPESP1]] | +0.61 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[DDX59-AS1]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[UGDH-AS1]] | +0.60 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[TMEM72-AS1]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CATSPER2P1]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[DICER1-AS1]] | +0.59 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[BRPF3-AS1]] | +0.59 | +0.58 / +0.46 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRPM2-AS]] | B | TRPM2-AS activity raises PPP1CB-DT's level | lines that do not express TRPM2-AS (29) vs lines expressing it (21) | 1.61× lower at baseline in the lines without TRPM2-AS | 0.026 | ⚠ within organs, on part of the lines; also absent: LINC03046, KLRC2, PCK1 |
| [[RDM1P5]] | B | RDM1P5 activity raises PPP1CB-DT's level | lines that do not express RDM1P5 (7) vs lines expressing it (43) | 1.61× lower at baseline in the lines without RDM1P5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000287022, TLCD3B, WWOX; maybe low, not absent |
| [[LINC02026]] | B | LINC02026 activity raises PPP1CB-DT's level | lines that do not express LINC02026 (8) vs lines expressing it (42) | 1.37× lower at baseline in the lines without LINC02026 | 0.087 | ⚠ within organs, on part of the lines; also absent: ASRGL1, ENSG00000256673 |
| [[SLC16A5]] | B | SLC16A5 activity raises PPP1CB-DT's level | lines that do not express SLC16A5 (15) vs lines expressing it (35) | 1.40× lower at baseline in the lines without SLC16A5 | 0.089 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TNFRSF10A, CDCP1 |
| [[DLX6-AS1]] | B | DLX6-AS1 activity raises PPP1CB-DT's level | lines that do not express DLX6-AS1 (23) vs lines expressing it (27) | 1.53× lower at baseline in the lines without DLX6-AS1 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000249776, FBXO27, KIF1A; maybe low, not absent |
| [[CARF]] | C | CARF's natural level strengthens PPP1CB-DT's drug response | CARF's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.53; direction not clear | 0.095 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.565). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (3.3, 22.3); signed map (32.9, -7.6). **Vector** length 61.0, 9.20% of its response variance represented; |z| ≥ 3 in 1,109 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +17.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +5.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.6 | +6.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +6.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +3.8 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +3.1 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | +1.2 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.7 | -8.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.3 | -12.8 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.8 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.4 | -1.5 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -1.4 | -2.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.2 | -1.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | PPP1CB divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p23.2 — chr2:28,707,511-28,751,722 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55829](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55829) · Entrez [112267877](https://www.ncbi.nlm.nih.gov/gene/112267877) · Ensembl [ENSG00000226833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000226833)

## Data

Gene col 13557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13557); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13557]; `tensor/DDL_lfc|DDL_z.npy` [13557]; `embed/gene_vectors.npy` [13557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13557 or target_col == 13557). Every well: [[PPP1CB-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PPP1CB-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
