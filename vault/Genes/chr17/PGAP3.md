---
symbol: "PGAP3"
type: "gene"
col: 8431
ensembl_id: "ENSG00000161395"
name: "post-GPI attachment to proteins phospholipase 3"
location: "17q12"
module: 46
arm: "+"
pooled_cpm: 5.37
n_lines_expressing: 48
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 4
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# PGAP3

*post-GPI attachment to proteins phospholipase 3* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.77× (z +7.0, q 2e-09, up in 4 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.31× (z +4.8, q 4e-04, up in 11 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (15 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.438× (z -10.5, q 6e-23, down in 19 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Panobinostat (drug)]] 0.05 µM: 0.568× (z -7.2, q 6e-11, down in 24 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED24]] (+0.63, fdr 1e-05), [[TTC31]] (+0.58, fdr 3e-05), [[NEIL1]] (+0.56, fdr 5e-05); moves opposite to [[NBEAL1]] (-0.56, fdr 4e-05), [[MIR4435-2HG]] (-0.53, fdr 5e-05), [[BACH1]] (-0.53, fdr 4e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ERBB2]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8431.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +7.0 | 2e-09 | 4/9 (BT-474, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +4.8 | 4e-04 | 11/35 (BT-474, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +4.5 | 0.001 | 3/32 (LoVo, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.39×** | +4.0 | 0.010 | 7/26 (A498, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.78×** | +3.8 | 0.014 | 0/12 | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.014 | 5/44 (BT-474, PANC-1, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.33×** | +3.6 | 0.025 | 3/18 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Afatinib (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.069 | 6/44 (BT-474, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[DT-061 (drug)]] 5 µM |  | 1.59× | +3.1 | 0.13 | 0/26 | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 15 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8431.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.438×** | -10.5 | 6e-23 | 19/32 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.472×** | -9.5 | 4e-19 | 34/45 (SK-MEL-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.499×** | -8.8 | 2e-16 | 30/45 (C-33 A, SK-MEL-2, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.500×** | -8.8 | 2e-16 | 26/45 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.518×** | -8.0 | 1e-13 | 23/43 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.568×** | -7.2 | 6e-11 | 24/45 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.581×** | -6.9 | 5e-10 | 20/37 (HT-29, A549, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.546×** | -6.4 | 1e-08 | 19/43 (A549, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -6.3 | 2e-08 | 19/43 (HT-29, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.554×** | -6.3 | 2e-08 | 16/43 (BT-474, SW1417, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -5.9 | 1e-07 | 14/44 (A549, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **0.639×** | -5.5 | 2e-06 | 16/29 (A-172, HOP62, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.600×** | -5.4 | 3e-06 | 15/44 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.644×** | -5.4 | 3e-06 | 12/37 (CHP-212, SW1417, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.788×** | -4.3 | 7e-04 | 18/37 (PANC-1, J82, …) | two highest doses | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.715×** | -4.3 | 7e-04 | 9/44 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.723×** | -3.9 | 0.003 | 10/41 (SW48, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.706×** | -3.7 | 0.007 | 9/43 (SW 900, HCT15, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.709×** | -3.6 | 0.008 | 11/39 (J82, COLO 205, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.821×** | -3.5 | 0.010 | 16/44 (RPMI-7951, HT-29, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **0.758×** | -3.4 | 0.018 | 6/43 (SW480, A549, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.611×** | -3.3 | 0.025 | 6/39 (SW48, A549, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.025 | 7/41 (SK-MEL-2, SW480, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.793×** | -2.9 | 0.068 | 7/43 (HepG2/C3A, AN3 CA, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.653×** | -2.8 | 0.091 | 4/42 (HT-29, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8431. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 6.95 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0533× (z -12.3) |
| [[LS 180 (line)]] | wt | 4.13 | 0 | 2 | — | [[Pemetrexed (drug)]] 5 µM 0.0481× (z -10.0) |
| [[A-172 (line)]] | wt | 3.09 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.05 µM 0.0654× (z -9.3) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H460 (line)]] | wt | 3.69 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.148× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[PANC-1 (line)]] | alt | 5.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -10.3) ⚠ cell-cycle shift, explains ~92% of this change |
| [[SK-MEL-2 (line)]] | alt | 3.63 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0414× (z -9.1) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SW1417 (line)]] | alt | 7.82 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0877× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.16 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.25 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.25 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.26 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.97 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.39 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.12 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.494 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.59 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.27 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8431), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 3 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED24]] | +0.63 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TTC31]] | +0.58 | +0.62 / +0.43 | both halves | 3e-05 |  |
| [[NEIL1]] | +0.56 | +0.52 / +0.39 | both halves | 5e-05 |  |
| [[RAF1]] | +0.56 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[STK11IP]] | +0.55 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[ECHDC2]] | +0.55 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[PMS2P1]] | +0.55 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[C14orf93]] | +0.54 | +0.45 / +0.46 | both halves | 3e-05 |  |
| [[TMEM94]] | +0.54 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[PGBD2]] | +0.53 | +0.55 / +0.39 | both halves | 6e-05 |  |
| [[TXNDC15]] | +0.53 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[POLDIP3]] | +0.52 | +0.45 / +0.53 | both halves | 3e-05 |  |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBEAL1]] | -0.56 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[MIR4435-2HG]] | -0.53 | -0.40 / -0.55 | both halves | 5e-05 |  |
| [[BACH1]] | -0.53 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[SH3BGRL3]] | -0.52 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[EHBP1]] | -0.51 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[WWC2]] | -0.49 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[CDK14]] | -0.48 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[ADAM32]] | -0.48 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SPEN]] | -0.48 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[ZFYVE28]] | -0.47 | -0.37 / -0.35 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.47 | -0.37 / -0.45 | both halves | 7e-05 |  |
| [[AGPAT4]] | -0.47 | -0.37 / -0.44 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERBB2]] | C | ERBB2 activity raises PGAP3's level | lines that do not express ERBB2 (3) vs lines expressing it (47) | 2.21× lower at baseline in the lines without ERBB2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: UGDH, IQSEC2, APOBEC3F; co-absent with the target; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.508). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-13.9, 8.1); signed map (-10.5, -30.1). **Vector** length 53.5, 7.03% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +4.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +4.5 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.2 | +2.9 |
| fall | [[Panobinostat (drug)]] 0.05 µM |  | -2.6 | -7.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.4 | -5.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -3.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.1 | -8.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.1 | -6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.0 | -6.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -3.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.4 | -2.6 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | post-GPI attachment to proteins phospholipase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:39,671,122-39,696,797 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9753, CAB2, PP1498, PER1; previously PERLD1 |
| Gene groups (HGNC) | CREST superfamily |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96FM1](https://www.uniprot.org/uniprotkb/Q96FM1) (GPI-specific phospholipase A2-like PGAP3):

> Involved in the fatty acid remodeling steps of GPI-anchor maturation where the unsaturated acyl chain at sn-2 of inositol phosphate is replaced by a saturated stearoyl chain. May catalyze the first step of the fatty acid remodeling, by removing the unsaturated acyl chain at sn-2 of inositol phosphate, generating a lyso-GPI intermediate (Probable). The fatty acid remodeling steps is critical for the integration of GPI-APs into lipid rafts (By similarity).

**Summary**, from NCBI Gene [93210](https://www.ncbi.nlm.nih.gov/gene/93210):

> This gene encodes a glycosylphosphatidylinositol (GPI)-specific phospholipase that primarily localizes to the Golgi apparatus. This ubiquitously expressed gene is predicted to encode a seven-transmembrane protein that removes unsaturated fatty acids from the sn-2 position of GPI. The remodeling of the constituent fatty acids on GPI is thought to be important for the proper association between GPI-anchored proteins and lipid rafts. The tethering of proteins to plasma membranes via …

**Accessions** — [HGNC:23719](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23719) · Entrez [93210](https://www.ncbi.nlm.nih.gov/gene/93210) · UniProt [Q96FM1](https://www.uniprot.org/uniprotkb/Q96FM1) · Ensembl [ENSG00000161395](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161395)

## Data

Gene col 8431: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8431); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8431, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8431]; `tensor/DDL_lfc|DDL_z.npy` [8431]; `embed/gene_vectors.npy` [8431]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8431 or target_col == 8431). Every well: [[PGAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
