---
symbol: "RXRB"
type: "gene"
col: 12834
ensembl_id: "ENSG00000204231"
name: "retinoid X receptor beta"
location: "6p21.32"
module: 138
arm: "+"
pooled_cpm: 20.15
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 20
n_dd_up_clean: 10
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/138"]
generated_by: "tahoemap"
---

# RXRB

*retinoid X receptor beta* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 1.64× (z +5.4, q 2e-05, up in 30 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.436× (z -12.8, q 1e-34, down in 45 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.631× (z -7.1, q 2e-10, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IKZF5]] (+0.66, fdr 1e-05), [[TEPSIN]] (+0.65, fdr 7e-06), [[GIGYF1]] (+0.64, fdr 8e-06); moves opposite to [[OLA1]] (-0.56, fdr 1e-05), [[GGCT]] (-0.54, fdr 3e-05), [[HSPD1]] (-0.54, fdr 2e-05).
> It is in [[Module 138]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIK3CA]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12834.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.64×** | +5.4 | 2e-05 | 30/47 (HEC-1-A, NCI-H2347, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.29×** | +5.4 | 2e-05 | 23/47 (SNU-423, LoVo, …) | rises with dose | composition shift |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.50×** | +4.5 | 0.001 | 20/45 (A498, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.69×** | +4.2 | 0.004 | 16/34 (NCI-H460, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +4.1 | 0.004 | 16/43 (A-427, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.004 | 14/47 (A498, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.30×** | +4.0 | 0.005 | 20/45 (PANC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.44×** | +4.0 | 0.005 | 15/44 (CFPAC-1, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.42×** | +3.8 | 0.008 | 14/47 (A-172, A549, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.28×** | +3.8 | 0.008 | 18/48 (NCI-H2030, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Gallic acid (hydrate) (drug)]] 0.5 µM |  | **1.29×** | +3.6 | 0.014 | 17/48 (HCT15, RKO, …) | inconsistent across doses | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.28×** | +3.6 | 0.018 | 16/47 (LoVo, SK-MEL-2, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.055 | 10/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +3.2 | 0.063 | 4/48 (A-172, HT-29, …) | inconsistent across doses | position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.077 | 9/46 (COLO 205, NCI-H23, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12834.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.436×** | -12.8 | 1e-34 | 45/48 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.575×** | -8.5 | 6e-15 | 33/48 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.606×** | -7.7 | 3e-12 | 36/48 (SW 900, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.624×** | -7.2 | 6e-11 | 36/48 (HEC-1-A, A498, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.631×** | -7.1 | 2e-10 | 33/48 (SW480, HOP62, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.450×** | -6.4 | 1e-08 | 33/47 (SW 900, HCT15, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.460×** | -6.2 | 4e-08 | 32/48 (NCI-H460, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.481×** | -5.9 | 3e-07 | 26/46 (NCI-H1792, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.518×** | -5.3 | 8e-06 | 27/46 (NCI-H2030, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.542×** | -4.9 | 5e-05 | 24/48 (PANC-1, NCI-H1573, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.745×** | -4.5 | 3e-04 | 17/48 (SW1417, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.677×** | -4.3 | 9e-04 | 19/48 (MIA PaCa-2, LoVo, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Adenosine (drug)]] 0.5 µM |  | **0.761×** | -3.9 | 0.005 | 9/48 (CFPAC-1, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.754×** | -3.7 | 0.008 | 15/37 (A549, NCI-H1573, …) | inconsistent across doses | composition shift; position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.631×** | -3.7 | 0.008 | 18/43 (RKO, RPMI-7951, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.659×** | -3.3 | 0.028 | 14/46 (Hs 766T, SW1417, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.664×** | -3.3 | 0.033 | 12/48 (A498, SNU-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | **0.813×** | -2.9 | 0.099 | 2/48 (SW480, AN3 CA) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.35 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12834. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 18.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.274× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~12% of this change |
| [[A498 (line)]] | wt | 17.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.282× (z -9.4) ⚠ unreliable plate only |
| [[A549 (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.228× (z -8.5) ⚠ unreliable plate only |
| [[C32 (line)]] | wt | 20.2 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.214× (z -8.7) |
| [[H4 (line)]] | wt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0473× (z -10.3) |
| [[J82 (line)]] | alt | 13.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.297× (z -10.5) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H1573 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 11.7 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.266× (z -9.5) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 20.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.364× (z -9.0) ⚠ unreliable plate only |
| [[SW 900 (line)]] | alt | 22.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.222× (z -9.2) ⚠ unreliable plate only |
| [[SW480 (line)]] | alt | 17.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.392× (z -8.7) |
| [[A-172 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12834), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IKZF5]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[TEPSIN]] | +0.65 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[GIGYF1]] | +0.64 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[TERF2IP]] | +0.61 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[GORASP1]] | +0.60 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RFX1]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[HNRNPH1]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CDK3]] | +0.59 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[WDR48]] | +0.59 | +0.40 / +0.66 | both halves | 5e-05 |  |
| [[RSF1]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[CHKB]] | +0.59 | +0.44 / +0.59 | both halves | 3e-05 |  |
| [[AKAP9]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OLA1]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GGCT]] | -0.54 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[HSPD1]] | -0.54 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[PAICS]] | -0.52 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[RPL6]] | -0.51 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[OPA1]] | -0.51 | -0.48 / -0.53 | both halves | 2e-05 |  |
| [[ENOPH1]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[BOLA3]] | -0.51 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[PTGES3]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 | pathway: Signaling by Nuclear Receptors |
| [[PSMD14]] | -0.50 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[NAA50]] | -0.50 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[IPO5]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIK3CA]] | B | PIK3CA activity lowers RXRB's level | compounds that target PIK3CA: 3 of 4 raise it (Alpelisib, Bimiralisib, GSK1059615) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 138]]; 34 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-12.4, -22.3); signed map (3.3, -8.1). **Vector** length 87.1, 18.5% of its response variance represented; |z| ≥ 3 in 766 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +4.8 | +3.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +4.2 | +5.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.4 | +5.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.3 | +4.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +4.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.5 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +2.8 | +3.8 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -12.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -4.8 | -6.4 |
|  | [[EX229 (drug)]] 5 µM |  | -4.6 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.6 | -7.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.2 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -4.2 | -6.2 |

## What is on record

|  |  |
|---|---|
| Name | retinoid X receptor beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,193,588-33,200,665 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NR2B2, H-2RIIBP, RCoR-1, RXRbeta, RXR-beta |
| Gene groups (HGNC) | Retinoid X receptors |
| Hallmark sets | UV_RESPONSE_UP |
| Reactome | 13 pathways, smallest: NR1H2 & NR1H3 regulate gene expression linked to triglyceride lipolysis in adipose; NR1H2 & NR1H3 regulate gene expression linked to gluconeogenesis; NR1H2 & NR1H3 regulate gene expression to limit cholesterol uptake |
| Matched by | ensembl_id |

**Function**, from UniProt [P28702](https://www.uniprot.org/uniprotkb/P28702) (Retinoic acid receptor RXR-beta):

> Receptor for retinoic acid. Retinoic acid receptors bind as heterodimers to their target response elements in response to their ligands, all-trans or 9-cis retinoic acid, and regulate gene expression in various biological processes. The RAR/RXR heterodimers bind to the retinoic acid response elements (RARE).

**Summary**, from NCBI Gene [6257](https://www.ncbi.nlm.nih.gov/gene/6257):

> This gene encodes a member of the retinoid X receptor (RXR) family of nuclear receptors which are involved in mediating the effects of retinoic acid (RA). The encoded protein forms homodimers with the retinoic acid, thyroid hormone, and vitamin D receptors, increasing both DNA binding and transcriptional function on their respective response elements. This gene lies within the major histocompatibility complex (MHC) class II region on chromosome 6. Alternatively spliced transcript variants …

**Accessions** — [HGNC:10478](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10478) · Entrez [6257](https://www.ncbi.nlm.nih.gov/gene/6257) · UniProt [P28702](https://www.uniprot.org/uniprotkb/P28702) · Ensembl [ENSG00000204231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204231)

## Data

Gene col 12834: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12834); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12834, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12834]; `tensor/DDL_lfc|DDL_z.npy` [12834]; `embed/gene_vectors.npy` [12834]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12834 or target_col == 12834). Every well: [[RXRB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RXRB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
