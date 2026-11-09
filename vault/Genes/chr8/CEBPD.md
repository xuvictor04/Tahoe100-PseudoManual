---
symbol: "CEBPD"
type: "gene"
col: 13310
ensembl_id: "ENSG00000221869"
name: "CCAAT enhancer binding protein delta"
location: "8q11.21"
module: 139
arm: "+"
pooled_cpm: 25.6
n_lines_expressing: 47
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 9
direction_downstream: 31
tags: ["gene", "module/139"]
generated_by: "tahoemap"
---

# CEBPD

*CCAAT enhancer binding protein delta* — 8q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 5.70× (z +9.6, q 4e-19, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.130× (z -11.7, q 6e-29, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PNRC1]] (+0.72, fdr 7e-06), [[BCL6]] (+0.71, fdr 7e-06), [[WTAP]] (+0.70, fdr 7e-06); moves opposite to [[DPP9]] (-0.64, fdr 1e-05), [[FXYD5]] (-0.63, fdr 3e-05), [[PSMD2]] (-0.62, fdr 1e-05).
> It is in [[Module 139]], a single-armed module (Interleukin-4 and Interleukin-13 signaling).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SAA2-SAA4]], [[SAA4]] → it (grade B ⚠); 31 go from it, the strongest it → cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13310.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **5.70×** | +9.6 | 4e-19 | 38/45 (PANC-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **2.45×** | +7.3 | 1e-10 | 30/45 (AsPC-1, J82, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **3.50×** | +6.9 | 9e-10 | 35/45 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **2.31×** | +4.8 | 2e-04 | 28/43 (PANC-1, J82, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **2.17×** | +4.3 | 0.002 | 28/44 (SHP-77, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.69×** | +4.3 | 0.002 | 26/45 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.10×** | +4.1 | 0.003 | 26/44 (SHP-77, HOP62, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.03×** | +4.0 | 0.004 | 24/45 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.93×** | +3.8 | 0.011 | 25/44 (SHP-77, HOP62, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.89×** | +3.7 | 0.014 | 27/45 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.87×** | +3.6 | 0.017 | 25/44 (SHP-77, HOP62, …) | inconsistent across doses | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.87×** | +3.6 | 0.017 | 26/44 (SHP-77, HOP62, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.78×** | +3.2 | 0.051 | 28/45 (AsPC-1, BT-474, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 0.05 µM |  | **1.74×** | +3.2 | 0.058 | 23/45 (SHP-77, HOP62, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13310.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.130×** | -11.7 | 6e-29 | 43/45 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.155×** | -10.7 | 3e-24 | 41/45 (BT-474, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.189×** | -9.6 | 2e-19 | 42/44 (SW 900, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.341×** | -6.2 | 8e-08 | 32/44 (C32, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.450×** | -4.6 | 5e-04 | 32/45 (HepG2/C3A, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.578×** | -4.5 | 8e-04 | 32/45 (C32, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.469×** | -4.4 | 0.001 | 31/45 (NCI-H2030, CHP-212, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.541×** | -3.3 | 0.059 | 23/44 (C32, PANC-1, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.350×** | -3.2 | 0.090 | 25/45 (SK-MEL-2, COLO 205, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.566×** | -3.2 | 0.090 | 26/43 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.581×** | -3.1 | 0.090 | 23/45 (HepG2/C3A, SK-MEL-2, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.584×** | -3.1 | 0.090 | 20/44 (Panc 03.27, SW480, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.76 per unit of S-phase module lfc, +0.88 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13310. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 92.0 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0401× (z -15.4) |
| [[HepG2_C3A (line)]] | wt | 82.7 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0517× (z -14.5) |
| [[A498 (line)]] | wt | 85.9 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.104× (z -11.2) |
| [[HS-578T (line)]] | alt | 25.4 | 3 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 20.9× (z +11.8) | [[Panobinostat (drug)]] 5 µM 0.0388× (z -13.0) |
| [[PANC-1 (line)]] | alt | 13.7 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 27.3× (z +14.3) | — |
| [[SHP-77 (line)]] | alt | 38.3 | 1 | 3 | [[Triamcinolone (drug)]] 5 µM 3.90× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.0736× (z -11.4) |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0242× (z -14.6) |
| [[SNU-423 (line)]] | alt | 30.8 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0390× (z -13.2) |
| [[SW 900 (line)]] | alt | 47.2 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 7.82× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.0867× (z -11.5) |
| [[A-172 (line)]] | wt | 15.4 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 6.60× (z +9.9) ⚠ cell-cycle shift, explains ~55% of this change | [[Panobinostat (drug)]] 5 µM 0.0396× (z -11.9) |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0130× (z -16.5) |
| [[CHP-212 (line)]] | wt | 56.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0645× (z -10.3) |
| [[COLO 205 (line)]] | alt | 39.1 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0158× (z -15.7) |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0321× (z -13.6) |
| [[J82 (line)]] | alt | 18.3 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +13.1) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 17.2× (z +10.8) | — |
| [[KATO III (line)]] | alt | 26.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.0734× (z -11.6) |
| [[LS 180 (line)]] | wt | 10.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0879× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 40.0 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0317× (z -14.8) |
| [[RPMI-7951 (line)]] | alt | 16.6 | 1 | 2 | [[Harringtonine (drug)]] 5 µM 20.4× (z +10.3) | [[Panobinostat (drug)]] 0.5 µM 0.0868× (z -8.6) |
| [[A549 (line)]] | wt | 34.2 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 7.64× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.0648× (z -12.0) |
| [[AsPC-1 (line)]] | alt | 20.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +15.2) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 20.8× (z +11.4) | — |
| [[HEC-1-A (line)]] | alt | 9.13 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 12.2× (z +9.6) | — |
| [[HOP62 (line)]] | alt | 7.90 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +12.0) ⚠ cell-cycle shift, explains ~55% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 23.8× (z +10.4) | — |
| [[LoVo (line)]] | wt | 12.9 | 1 | 1 | [[Harringtonine (drug)]] 5 µM 9.84× (z +8.9) | [[Panobinostat (drug)]] 5 µM 0.0901× (z -9.6) |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 1 (1 ⚠) | 1 | [[Adagrasib (drug)]] 0.05 µM 1.86× (z +8.5) ⚠ position not correctable | [[Panobinostat (drug)]] 0.5 µM 0.0809× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 45.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.176× (z -8.5) |
| [[Panc 03.27 (line)]] | alt | 43.7 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0351× (z -14.5) |
| [[SW480 (line)]] | alt | 12.3 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0710× (z -11.2) |
| [[hTERT-HPNE (line)]] | wt | 29.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0555× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 19.2 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 9.98× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 37.4 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 8.26× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 16.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0602× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.145× (z -8.6) |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.52 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.51 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.45 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13310), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PNRC1]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[BCL6]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 764 |
| [[WTAP]] | +0.70 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[TMEM265]] | +0.69 | +0.60 / +0.70 | both halves | 7e-06 |  |
| [[MT1M]] | +0.69 | +0.73 / +0.61 | both halves | 7e-06 |  |
| [[NNMT]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[SAA2-SAA4]] | +0.68 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[ZFP36L1]] | +0.68 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[NFKBIA]] | +0.67 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 489 |
| [[STAT5A]] | +0.65 | +0.60 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[SCAF11]] | +0.65 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[SAA4]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPP9]] | -0.64 | -0.62 / -0.55 | both halves | 1e-05 |  |
| [[FXYD5]] | -0.63 | -0.73 / -0.46 | both halves | 3e-05 |  |
| [[PSMD2]] | -0.62 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[AGO1]] | -0.61 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[AP3M2]] | -0.61 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[BCAP31]] | -0.61 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[PPM1F]] | -0.58 | -0.58 / -0.46 | both halves | 2e-05 |  |
| [[MMP1]] | -0.57 | -0.68 / -0.46 | both halves | 3e-05 | pathway: Interleukin-4 and Interleukin-13 signaling |
| [[ATP13A2]] | -0.57 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[FBXW2]] | -0.57 | -0.60 / -0.47 | both halves | 2e-05 |  |
| [[SFRP1]] | -0.57 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[MTPN]] | -0.56 | -0.59 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAA2-SAA4]], [[SAA4]] | B | SAA2-SAA4, SAA4 activity raises CEBPD's level | lines that do not express SAA2-SAA4, SAA4 (22) vs lines expressing them (28) | 1.86× lower at baseline in the lines without SAA2-SAA4, SAA4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA1, LMO2; co-absent genes |
| [[BATF]] | B | BATF activity raises CEBPD's level | lines that do not express BATF (33) vs lines expressing it (17) | 1.79× lower at baseline in the lines without BATF | 0.047 | ⚠ within organs, on part of the lines; also absent: KRT23, WFDC2, TACSTD2 |
| [[SAA2]] | B | SAA2 activity raises CEBPD's level | lines that do not express SAA2 (20) vs lines expressing it (30) | 1.91× lower at baseline in the lines without SAA2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SAA4, SAA1, NEURL3 |
| [[STAT5A]] | B | STAT5A activity raises CEBPD's level | lines that do not express STAT5A (12) vs lines expressing it (38) | 2.02× lower at baseline in the lines without STAT5A | 0.068 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LGALS3, NOD2, ETS2 |
| [[GBP1]] | B | GBP1 activity raises CEBPD's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.25× lower at baseline in the lines without GBP1 | 0.077 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[PLPP3]] | B | PLPP3 activity raises CEBPD's level | lines that do not express PLPP3 (5) vs lines expressing it (45) | 1.31× lower at baseline in the lines without PLPP3 | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000284686; maybe low, not absent |
| [[CP]] | B | CP activity raises CEBPD's level | lines that do not express CP (39) vs lines expressing it (11) | 2.24× lower at baseline in the lines without CP | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[TNFSF14]] | B | TNFSF14 activity raises CEBPD's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without TNFSF14 | 0.096 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[PSMB8]] | C | PSMB8 activity raises CEBPD's level | lines that do not express PSMB8 (4) vs lines expressing it (46) | 4.88× lower at baseline in the lines without PSMB8 | 0.004 | ⚠ few lines (4 vs 46); across organs; co-occurs with WNK2; also absent: TBILA, GCA, C3orf52; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tetracycline (hydrochloride) (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Tetracycline (hydrochloride) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.67× the cells of the other lines | 0.006 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Quinidine (15% dihydroquinidine) (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Quinidine (15% dihydroquinidine) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.69× the cells of the other lines | 0.010 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Sulfatinib (drug)]] 5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Sulfatinib 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.65× the cells of the other lines | 0.021 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Entecavir (monohydrate) (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Entecavir (monohydrate) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.66× the cells of the other lines | 0.026 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.40× the cells of the other lines | 0.029 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Cepharanthine (drug)]] 5 µM | C | CEBPD, [[GCA]] activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 1.30× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Bisoprolol (hemifumarate) 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.031 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.54× the cells of the other lines | 0.035 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Tranilast (drug)]] 0.5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Tranilast 0.5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.74× the cells of the other lines | 0.036 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Niclosamide (olamine) (drug)]] 5 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Niclosamide (olamine) 5 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.36× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |
| cells under [[Cyclosporin A (drug)]] 0.05 µM | C | CEBPD, [[GCA]] activity raises the cells' numbers under Cyclosporin A 0.05 µM (protects the cells) | lines that do not express CEBPD, GCA (3) vs lines expressing them (45) | the lines without CEBPD, GCA: 0.66× the cells of the other lines | 0.038 | ⚠ few lines (3 vs 47); tissue-confounded; across organs; also absent: LRRCC1, PSMB8, SDC4; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 139]] — Interleukin-4 and Interleukin-13 signaling; 34 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (26.4, 15.5); signed map (16.4, 28.2). **Vector** length 144, 52.3% of its response variance represented; |z| ≥ 3 in 1,120 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.51 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +12.2 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +11.5 | +9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +7.7 | +4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.0 | +6.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +5.5 | +3.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +5.4 | +3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +4.9 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.4 | +2.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.2 | -6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.0 | -0.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.9 | -11.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.8 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.6 | -10.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.4 | -3.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -2.9 | -2.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | CCAAT enhancer binding protein delta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.21 — chr8:47,736,913-47,738,164 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRP3, CELF, C/EBP-delta, NF-IL6-beta |
| Gene groups (HGNC) | CCAAT/enhancer binding proteins |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 8 pathways, smallest: HCMV Late Events; Transcriptional regulation of white adipocyte differentiation; Interleukin-4 and Interleukin-13 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P49716](https://www.uniprot.org/uniprotkb/P49716) (CCAAT/enhancer-binding protein delta):

> Transcription activator that recognizes two different DNA motifs: the CCAAT homology common to many promoters and the enhanced core homology common to many enhancers. Important transcription factor regulating the expression of genes involved in immune and inflammatory responses. Transcriptional activator that enhances IL6 transcription alone and as heterodimer with CEBPB.

**Summary**, from NCBI Gene [1052](https://www.ncbi.nlm.nih.gov/gene/1052):

> The protein encoded by this intronless gene is a bZIP transcription factor which can bind as a homodimer to certain DNA regulatory regions. It can also form heterodimers with the related protein CEBP-alpha. The encoded protein is important in the regulation of genes involved in immune and inflammatory responses, and may be involved in the regulation of genes associated with activation and/or differentiation of macrophages. The cytogenetic location of this locus has been reported as both 8p11 …

**Accessions** — [HGNC:1835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1835) · Entrez [1052](https://www.ncbi.nlm.nih.gov/gene/1052) · UniProt [P49716](https://www.uniprot.org/uniprotkb/P49716) · Ensembl [ENSG00000221869](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000221869)

## Data

Gene col 13310: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13310); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13310, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13310]; `tensor/DDL_lfc|DDL_z.npy` [13310]; `embed/gene_vectors.npy` [13310]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13310 or target_col == 13310). Every well: [[CEBPD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEBPD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
