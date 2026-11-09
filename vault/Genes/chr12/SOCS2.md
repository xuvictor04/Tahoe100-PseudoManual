---
symbol: "SOCS2"
type: "gene"
col: 4226
ensembl_id: "ENSG00000120833"
name: "suppressor of cytokine signaling 2"
location: "12q22"
module: 68
arm: "+"
pooled_cpm: 8.02
n_lines_expressing: 40
n_dd_up: 27
n_dd_down: 14
n_dd_up_clean: 14
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 4
direction_downstream: 9
tags: ["gene", "module/068"]
generated_by: "tahoemap"
---

# SOCS2

*suppressor of cytokine signaling 2* — 12q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.29× (z +24.2, q 0e+00, up in 27 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.536× (z -7.3, q 1e-10, down in 20 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SOCS2-AS1]] (+0.83, fdr 7e-06, ⚠ same locus), [[FAM200B]] (+0.67, fdr 1e-05), [[PLA2G4C]] (+0.67, fdr 8e-06), [[TEF]] (+0.65, fdr 1e-05); moves opposite to [[TYW1]] (-0.59, fdr 1e-05), [[ZDHHC9]] (-0.59, fdr 1e-05), [[TTLL5]] (-0.58, fdr 3e-05).
> It sits in the **+** arm of [[Module 068]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 9 go from it, the strongest it → [[APLF]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4226.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.29×** | +24.2 | 0e+00 | 27/31 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **5.39×** | +18.0 | 0e+00 | 33/35 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.80×** | +15.7 | 0e+00 | 28/32 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.61×** | +11.3 | 2e-27 | 26/36 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.9 | 3e-13 | 9/15 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.58×** | +7.6 | 4e-12 | 22/36 (LoVo, C32, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.97×** | +7.2 | 4e-11 | 11/21 (A498, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.73×** | +6.4 | 9e-09 | 17/32 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +6.1 | 5e-08 | 8/20 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.73×** | +5.8 | 3e-07 | 16/24 (PANC-1, A549, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.59×** | +5.4 | 3e-06 | 16/35 (J82, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +5.4 | 4e-06 | 15/35 (A549, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.45×** | +4.3 | 7e-04 | 11/37 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **1.44×** | +4.3 | 8e-04 | 7/24 (A549, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.43×** | +3.8 | 0.006 | 1/11 (PANC-1) | all doses, flat | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.7 | 0.007 | 7/37 (LoVo, A498, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.78×** | +3.6 | 0.012 | 2/23 (A549, NCI-H1792) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.75×** | +3.4 | 0.019 | 6/29 (A-172, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Atazanavir (sulfate) (drug)]] 0.5 µM |  | **1.33×** | +3.3 | 0.023 | 3/34 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **1.68×** | +3.2 | 0.036 | 2/28 (A498, A-172) | top dose only | noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.66×** | +3.1 | 0.047 | 1/28 (A-172) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.053 | 7/38 (LoVo, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4226.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.536×** | -7.3 | 1e-10 | 20/35 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.598×** | -6.1 | 4e-07 | 19/37 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.638×** | -5.3 | 2e-05 | 15/37 (H4, hTERT-HPNE, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.664×** | -4.5 | 0.001 | 6/32 (NCI-H460, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.695×** | -4.3 | 0.002 | 12/37 (NCI-H460, Hs 766T, …) | top dose only |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.708×** | -4.1 | 0.004 | 12/35 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.721×** | -3.9 | 0.009 | 10/37 (hTERT-HPNE, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.725×** | -3.8 | 0.010 | 8/34 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.804×** | -3.7 | 0.016 | 9/37 (H4, A498, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.016 | 10/37 (NCI-H460, A498, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.576×** | -3.4 | 0.034 | 10/29 (Hs 766T, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.754×** | -3.3 | 0.040 | 10/31 (AsPC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.049 | 15/36 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.774×** | -3.0 | 0.098 | 10/36 (hTERT-HPNE, NCI-H460, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4226. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 37.0 | 4 | 2 | [[Homoharringtonine (drug)]] 5 µM 4.18× (z +13.7) | [[Panobinostat (drug)]] 5 µM 0.178× (z -11.7) |
| [[PANC-1 (line)]] | alt | 11.4 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.35× (z +23.6) | — |
| [[A498 (line)]] | wt | 10.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.4× (z +21.4) | — |
| [[A549 (line)]] | wt | 11.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.99× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 5.35 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.1× (z +14.9) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0974× (z -8.6) |
| [[J82 (line)]] | alt | 2.82 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 25.6× (z +13.4) | — |
| [[LoVo (line)]] | wt | 16.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +10.4) | — |
| [[NCI-H2030 (line)]] | alt | 33.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.37× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 24.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +9.8) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.105× (z -12.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 16.4 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 4.93× (z +8.9) | [[Trametinib (drug)]] 0.5 µM 0.257× (z -9.3) |
| [[Hs 766T (line)]] | wt | 7.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +11.5) | — |
| [[NCI-H1573 (line)]] | alt | 3.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.92× (z +9.0) | — |
| [[SNU-423 (line)]] | alt | 4.32 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +12.7) | — |
| [[A-427 (line)]] | wt | 4.29 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.39 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.630 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.11 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.885 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.65 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.867 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4226), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SOCS2-AS1]] | +0.83 | +0.81 / +0.76 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[FAM200B]] | +0.67 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[PLA2G4C]] | +0.67 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[TEF]] | +0.65 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[RIPK2-DT]] | +0.64 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[S100A3]] | +0.63 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[SYNPO]] | +0.63 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[FAM200A]] | +0.62 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[MMRN2]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[APLF]] | +0.60 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[TRAF1]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING |
| [[ZNF702P]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[SERTAD4]] | +0.60 | +0.56 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | -0.59 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[ZDHHC9]] | -0.59 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[TTLL5]] | -0.58 | -0.58 / -0.44 | both halves | 3e-05 |  |
| [[PDPR2P]] | -0.58 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[STRAP]] | -0.58 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[TNPO3]] | -0.58 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[PHKA2]] | -0.57 | -0.51 / -0.50 | both halves | 1e-05 |  |
| [[CTNNBL1]] | -0.56 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[ZCCHC17]] | -0.55 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[EIF3K]] | -0.55 | -0.47 / -0.40 | both halves | 4e-05 |  |
| [[ATRN]] | -0.55 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[NME2]] | -0.54 | -0.57 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers SOCS2's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[SPHK1]] | B | SPHK1 activity raises SOCS2's level | lines that do not express SPHK1 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without SPHK1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMEM158, CAV1, NR3C1 |
| [[ZFY]] | B | ZFY activity raises SOCS2's level | lines that do not express ZFY (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without ZFY | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PRKY, RPS4Y1, LINC00278 |
| [[SOCS2-AS1]] | C | SOCS2-AS1 activity raises SOCS2's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 3.29× lower at baseline in the lines without SOCS2-AS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLF]] | B | SOCS2 activity raises APLF's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 2.32× lower at baseline in the lines without SOCS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[ARL14EP]] | B | SOCS2 activity raises ARL14EP's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.48× lower at baseline in the lines without SOCS2 | 0.014 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[FMNL3]] | B | SOCS2 activity raises FMNL3's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 3.27× lower at baseline in the lines without SOCS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[NFKB2]] | B | SOCS2 activity raises NFKB2's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.49× lower at baseline in the lines without SOCS2 | 0.039 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[SIX5]] | B | SOCS2 activity raises SIX5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.43× lower at baseline in the lines without SOCS2 | 0.050 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[SPHK1]] | B | SOCS2 activity raises SPHK1's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 2.91× lower at baseline in the lines without SOCS2 | 0.077 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[ZBED5]] | B | SOCS2 activity raises ZBED5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.31× lower at baseline in the lines without SOCS2 | 0.080 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[SOCS5]] | B | SOCS2 activity raises SOCS5's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without SOCS2 | 0.097 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A |
| [[SOCS2-AS1]] | C | SOCS2 activity raises SOCS2-AS1's level | lines that do not express SOCS2 (10) vs lines expressing it (40) | 3.17× lower at baseline in the lines without SOCS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, HOXC9, TMEM45A; co-absent with the target |

## Where it sits

- **Module**: [[Module 068]]; 73 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.43).
- **Nodal map** (x, y) = (17.4, 9.6); signed map (27.6, 7.2). **Vector** length 72.1, 14.1% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.3 | +24.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.7 | +18.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.1 | +15.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.6 | +7.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +5.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.2 | +1.5 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -6.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.5 | -3.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.5 | -7.3 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -3.0 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | suppressor of cytokine signaling 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q22 — chr12:93,569,814-93,583,487 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STATI2, SSI2, SOCS-2, SSI-2, CIS2, Cish2 |
| Gene groups (HGNC) | SH2 domain containing; Suppressors of cytokine signaling |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 7 pathways, smallest: Negative regulation of FLT3; Growth hormone receptor signaling; Interleukin-7 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O14508](https://www.uniprot.org/uniprotkb/O14508) (Suppressor of cytokine signaling 2):

> Substrate-recognition component of a cullin-5-RING E3 ubiquitin-protein ligase complex (ECS complex, also named CRL5 complex), which mediates the ubiquitination and subsequent proteasomal degradation of target proteins, such as EPOR and GHR. Specifically recognizes and binds phosphorylated proteins via its SH2 domain, promoting their ubiquitination. The ECS(SOCS2) complex acts as a key regulator of growth hormone receptor (GHR) levels by mediating ubiquitination and degradation of GHR, …

**Summary**, from NCBI Gene [8835](https://www.ncbi.nlm.nih.gov/gene/8835):

> This gene encodes a member of the suppressor of cytokine signaling (SOCS) family. SOCS family members are cytokine-inducible negative regulators of cytokine receptor signaling via the Janus kinase/signal transducer and activation of transcription pathway (the JAK/STAT pathway). SOCS family proteins interact with major molecules of signaling complexes to block further signal transduction, in part, by proteasomal depletion of receptors or signal-transducing proteins via ubiquitination. The …

**Accessions** — [HGNC:19382](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19382) · Entrez [8835](https://www.ncbi.nlm.nih.gov/gene/8835) · UniProt [O14508](https://www.uniprot.org/uniprotkb/O14508) · Ensembl [ENSG00000120833](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120833)

## Data

Gene col 4226: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4226); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4226, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4226]; `tensor/DDL_lfc|DDL_z.npy` [4226]; `embed/gene_vectors.npy` [4226]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4226 or target_col == 4226). Every well: [[SOCS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SOCS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
