---
symbol: "TCF19"
type: "gene"
col: 6000
ensembl_id: "ENSG00000137310"
name: "transcription factor 19"
location: "6p21.33"
module: 6
arm: "+"
pooled_cpm: 6.67
n_lines_expressing: 45
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 4
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 6
direction_downstream: 91
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TCF19

*transcription factor 19* — 6p21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (18 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.98× (z +12.9, q 2e-35, up in 8 of 11 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.48× (z +3.8, q 0.006, up in 3 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.424× (z -11.8, q 2e-29, down in 30 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GINS2]] (+0.88, fdr 7e-06), [[EXO1]] (+0.84, fdr 7e-06), [[TK1]] (+0.84, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); 91 go from it, the strongest it → [[PCLAF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 18 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6000.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **3.98×** | +12.9 | 2e-35 | 8/11 (A-172, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **3.36×** | +11.8 | 1e-29 | 34/42 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **3.29×** | +11.6 | 9e-29 | 37/42 (SW480, NCI-H23, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **3.01×** | +10.7 | 1e-24 | 35/41 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **2.56×** | +9.2 | 6e-18 | 20/21 (HS-578T, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | **2.64×** | +8.7 | 2e-16 | 5/14 (HS-578T, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.87×** | +6.1 | 8e-08 | 15/42 (SW480, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +5.1 | 2e-05 | 8/29 (CFPAC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~25% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.66×** | +4.7 | 1e-04 | 11/34 (SW480, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.63×** | +4.6 | 2e-04 | 14/35 (SW480, HS-578T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.56×** | +4.4 | 7e-04 | 15/36 (LoVo, HT-29, …) | rises with dose | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.55×** | +4.3 | 8e-04 | 15/41 (SW480, PANC-1, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~78% of this change | **1.52×** | +4.1 | 0.002 | 8/42 (SW480, HT-29, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.48×** | +3.8 | 0.006 | 3/41 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.31×** | +3.7 | 0.009 | 14/43 (SW480, HT-29, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.02×** | +3.6 | 0.011 | 4/40 (SW480, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.029 | 5/39 (SW480, LS 180, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.39×** | +3.0 | 0.072 | 6/41 (RKO, NCI-H460, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6000.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.424×** | -11.8 | 2e-29 | 30/37 (A498, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.428×** | -8.3 | 4e-14 | 25/35 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.512×** | -6.1 | 1e-07 | 23/39 (HEC-1-A, A-172, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.546×** | -5.9 | 6e-07 | 21/42 (NCI-H23, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.604×** | -4.9 | 1e-04 | 17/39 (NCI-H460, LS 180, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.618×** | -4.7 | 3e-04 | 17/42 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.625×** | -4.6 | 4e-04 | 20/35 (NCI-H2030, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.632×** | -4.5 | 6e-04 | 17/41 (J82, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.669×** | -3.9 | 0.006 | 17/41 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.587×** | -3.7 | 0.013 | 12/43 (KATO III, A-427, …) | inconsistent across doses | noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.590×** | -3.7 | 0.013 | 4/43 (SW 900, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.779×** | -3.4 | 0.029 | 11/43 (RKO, KATO III, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.701×** | -3.3 | 0.048 | 7/42 (CFPAC-1, HS-578T, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.721×** | -3.2 | 0.059 | 10/43 (hTERT-HPNE, Hs 766T, …) | all doses, flat |  |
| [[Sapanisertib (drug)]] 5 µM |  | **0.547×** | -3.1 | 0.076 | 4/43 (LS 180, HOP62, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[BAY1125976 (drug)]] 5 µM |  | **0.547×** | -3.1 | 0.076 | 6/43 (LS 180, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.734×** | -3.0 | 0.090 | 7/42 (KATO III, HEC-1-A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.46 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6000. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0452× (z -14.3) |
| [[A498 (line)]] | wt | 14.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -18.2) |
| [[Hs 766T (line)]] | wt | 6.45 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0589× (z -14.3) |
| [[A-427 (line)]] | wt | 13.2 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.229× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 13.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.182× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 6.72 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0728× (z -10.6) ⚠ toxic |
| [[RKO (line)]] | wt | 7.81 | 0 | 1 | — | [[Estrone sulfate (potassium) (drug)]] 0.5 µM 0.0921× (z -8.8) |
| [[SW480 (line)]] | alt | 5.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -9.7) |
| [[A549 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.87 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.05 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 8.86 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.47 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.46 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6000), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GINS2]] | +0.88 | +0.84 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[EXO1]] | +0.84 | +0.78 / +0.86 | both halves | 7e-06 |  |
| [[TK1]] | +0.84 | +0.80 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM4]] | +0.83 | +0.78 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MYBL2]] | +0.83 | +0.79 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[WDR76]] | +0.82 | +0.76 / +0.86 | both halves | 7e-06 | STRING 421 |
| [[DSCC1]] | +0.82 | +0.74 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[DTL]] | +0.82 | +0.75 / +0.86 | both halves | 7e-06 |  |
| [[MCM10]] | +0.81 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[CDC6]] | +0.81 | +0.70 / +0.83 | both halves | 7e-06 |  |
| [[CDC45]] | +0.81 | +0.72 / +0.85 | both halves | 7e-06 |  |
| [[MMS22L]] | +0.80 | +0.72 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 1, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises TCF19's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.91× lower at baseline in the lines without CDC25A | 0.087 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises TCF19's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises TCF19's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.60× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.081 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[MELK]], [[TK1]] | C | MELK, TK1 activity raises TCF19's level | lines that do not express MELK, TK1 (3) vs lines expressing them (47) | 2.68× lower at baseline in the lines without MELK, TK1 | 0.084 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |
| [[CLSPN]] | C | CLSPN activity raises TCF19's level | lines that do not express CLSPN (4) vs lines expressing it (46) | 2.65× lower at baseline in the lines without CLSPN | 0.087 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, CDC45, RRM2; maybe low, not absent; co-absent with the target |
| [[MYBL2]] | C | MYBL2 activity raises TCF19's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.28× lower at baseline in the lines without MYBL2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 79, C 12. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCLAF]] | B | TCF19 activity raises PCLAF's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.52× lower at baseline in the lines without TCF19 | 0.002 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[BRIP1]] | B | TCF19 activity raises BRIP1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.01× lower at baseline in the lines without TCF19 | 0.003 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[LIG1]] | B | TCF19 activity raises LIG1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.24× lower at baseline in the lines without TCF19 | 0.006 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CENPU]] | B | TCF19 activity raises CENPU's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.28× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MCM4]] | B | TCF19 activity raises MCM4's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[UBE2T]] | B | TCF19 activity raises UBE2T's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.30× lower at baseline in the lines without TCF19 | 0.008 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[GINS1]] | B | TCF19 activity raises GINS1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without TCF19 | 0.009 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[TUBB]] | B | TCF19 activity raises TUBB's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 1.70× lower at baseline in the lines without TCF19 | 0.010 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[PCNA]] | B | TCF19 activity raises PCNA's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.38× lower at baseline in the lines without TCF19 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[ZWINT]] | B | TCF19 activity raises ZWINT's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.33× lower at baseline in the lines without TCF19 | 0.011 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[SPC24]] | B | TCF19 activity raises SPC24's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.42× lower at baseline in the lines without TCF19 | 0.012 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[XRCC2]] | B | TCF19 activity raises XRCC2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.58× lower at baseline in the lines without TCF19 | 0.013 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.862). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.5, -44.7); signed map (-37.9, -44.5). **Vector** length 91.7, 21.1% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.69 to 28); *DNA Replication* (reactome, mean cos +0.68 to 40); *E2F G1/S* (control, mean cos +0.69 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.3 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~73% of this change | +4.0 | +10.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | +3.9 | +11.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +3.7 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~72% of this change | +3.4 | +8.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +3.8 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +3.0 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.7 | +2.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.9 | -11.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.6 | -8.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.0 | -6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~58% of this change | -4.0 | -4.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -1.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | transcription factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.33 — chr6:31,158,331-31,167,159 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SC1 |
| Gene groups (HGNC) | PHD finger proteins |
| Hallmark sets | E2F_TARGETS |
| Reactome | 6 pathways, smallest: Interaction of NuRD complexes with transcription factors; NuRD complex assembly; CHD3, CHD4, CHD5 subfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y242](https://www.uniprot.org/uniprotkb/Q9Y242) (Transcription factor 19):

> Potential transcription factor that may play a role in the regulation of genes involved in cell cycle G1/S transition. May bind to regulatory elements of genes, including the promoter of the transcription factor FOXO1.

**Summary**, from NCBI Gene [6941](https://www.ncbi.nlm.nih.gov/gene/6941):

> This gene encodes a protein that contains a PHD-type zinc finger domain and likely functions as a transcription factor. The encoded protein plays a role proliferation and apoptosis of pancreatic beta cells. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:11629](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11629) · Entrez [6941](https://www.ncbi.nlm.nih.gov/gene/6941) · UniProt [Q9Y242](https://www.uniprot.org/uniprotkb/Q9Y242) · Ensembl [ENSG00000137310](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137310)

## Data

Gene col 6000: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6000); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6000, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6000]; `tensor/DDL_lfc|DDL_z.npy` [6000]; `embed/gene_vectors.npy` [6000]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6000 or target_col == 6000). Every well: [[TCF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TCF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
