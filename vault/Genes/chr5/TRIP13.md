---
symbol: "TRIP13"
type: "gene"
col: 986
ensembl_id: "ENSG00000071539"
name: "thyroid hormone receptor interactor 13"
location: "5p15.33"
module: 6
arm: "+"
pooled_cpm: 24.2
n_lines_expressing: 49
n_dd_up: 14
n_dd_down: 20
n_dd_up_clean: 4
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# TRIP13

*thyroid hormone receptor interactor 13* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.55× (z +15.3, q 0e+00, up in 27 of 31 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.56× (z +5.5, q 4e-06, up in 26 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.628× (z -5.8, q 4e-06, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CENPH]] (+0.81, fdr 7e-06), [[KNTC1]] (+0.78, fdr 7e-06), [[XRCC2]] (+0.78, fdr 7e-06); moves opposite to [[SAT2]] (-0.68, fdr 7e-06), [[CCDC126]] (-0.65, fdr 7e-06), [[SMIM26]] (-0.63, fdr 7e-06, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[DCTN6-DT]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 986.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.55×** | +15.3 | 0e+00 | 27/31 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **3.12×** | +14.2 | 1e-43 | 35/39 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.17×** | +8.9 | 7e-17 | 30/36 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +7.3 | 3e-11 | 15/47 (J82, A-427, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +5.5 | 4e-06 | 26/46 (MIA PaCa-2, NCI-H460, …) | top dose only | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.55×** | +5.5 | 4e-06 | 28/46 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.50×** | +5.1 | 3e-05 | 26/47 (NCI-H1792, CFPAC-1, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~71% of this change | **1.39×** | +4.0 | 0.005 | 21/45 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.45×** | +4.0 | 0.005 | 17/43 (LS 180, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.37×** | +3.7 | 0.011 | 14/46 (HOP62, NCI-H460, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.6 | 0.019 | 13/27 (SNU-423, NCI-H2347, …) | rises with dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.72×** | +3.5 | 0.020 | 18/45 (NCI-H460, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.32×** | +3.4 | 0.031 | 12/47 (KATO III, SW480, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.21×** | +3.4 | 0.033 | 14/47 (SHP-77, PANC-1, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.075 | 15/46 (HOP62, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 986.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.628×** | -5.8 | 4e-06 | 28/47 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.643×** | -5.6 | 7e-06 | 25/47 (BT-474, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -5.4 | 1e-05 | 25/46 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.628×** | -5.1 | 5e-05 | 27/47 (LS 180, LOX-IMVI, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.684×** | -4.8 | 2e-04 | 23/45 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.772×** | -4.6 | 3e-04 | 21/47 (J82, LS 180, …) | two highest doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.708×** | -4.4 | 1e-03 | 19/47 (J82, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.723×** | -4.1 | 0.003 | 21/45 (HEC-1-A, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.728×** | -4.0 | 0.004 | 24/47 (A-427, RKO, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.777×** | -3.8 | 0.009 | 17/47 (HEC-1-A, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.813×** | -3.7 | 0.011 | 17/47 (HT-29, Panc 03.27, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.740×** | -3.7 | 0.011 | 16/45 (C32, HEC-1-A, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.816×** | -3.7 | 0.011 | 21/47 (A-427, A498, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.011 | 13/47 (HEC-1-A, A-427, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.578×** | -3.6 | 0.011 | 19/37 (MIA PaCa-2, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.690×** | -3.3 | 0.028 | 11/47 (Hs 766T, SW 1271, …) | all doses, flat | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 5 µM |  | 0.836× | -3.2 | 0.036 | 9/47 (NCI-H460, SK-MEL-2, …) | rises with dose | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **0.641×** | -2.9 | 0.087 | 9/46 (A-427, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 0.842× | -2.9 | 0.087 | 12/47 (HEC-1-A, A-427, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.57 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 986. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 32.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.04× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -15.1) |
| [[A-427 (line)]] | wt | 58.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -19.0) |
| [[A498 (line)]] | wt | 39.6 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 17.3 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.12× (z +13.0) | — |
| [[H4 (line)]] | wt | 26.2 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 22.0 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.8) | — |
| [[A-172 (line)]] | wt | 26.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.42× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Belinostat (drug)]] 0.5 µM 0.253× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 20.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.40× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -13.1) |
| [[HS-578T (line)]] | alt | 24.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 32.1 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Bortezomib (drug)]] 5 µM 0.0586× (z -9.2) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 15.6 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +13.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[PANC-1 (line)]] | alt | 29.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SNU-423 (line)]] | alt | 10.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.148× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 29.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.150× (z -9.8) |
| [[Hs 766T (line)]] | wt | 29.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.45× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 8.56 | 0 | 1 | — | [[Cepharanthine (drug)]] 0.5 µM 0.0671× (z -8.8) |
| [[J82 (line)]] | alt | 51.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[RPMI-7951 (line)]] | alt | 17.1 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.103× (z -10.6) |
| [[AN3 CA (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.87 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 986), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CENPH]] | +0.81 | +0.78 / +0.77 | both halves | 7e-06 | STRING 511 |
| [[KNTC1]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | STRING 617 |
| [[XRCC2]] | +0.78 | +0.69 / +0.82 | both halves | 7e-06 |  |
| [[VRK1]] | +0.77 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[ZWILCH]] | +0.76 | +0.67 / +0.76 | both halves | 7e-06 | STRING 625 |
| [[POLE]] | +0.75 | +0.70 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[FANCG]] | +0.75 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[FANCD2]] | +0.75 | +0.69 / +0.80 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 512 |
| [[RRM2]] | +0.75 | +0.74 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 674 |
| [[MCM4]] | +0.74 | +0.69 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 741 |
| [[CENPK]] | +0.72 | +0.68 / +0.78 | both halves | 7e-06 | STRING 453 |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAT2]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[CCDC126]] | -0.65 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.63 | -0.63 / -0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[DCTN6-DT]] | -0.61 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.61 | -0.59 / -0.60 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity raises TRIP13's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[DSCC1]] | C | DSCC1 activity raises TRIP13's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.20× lower at baseline in the lines without DSCC1 | 0.032 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.753). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-37.8, -44.4); signed map (-38.7, -48.0). **Vector** length 118, 32.5% of its response variance represented; |z| ≥ 3 in 1,055 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.59 to 28); *DNA Replication* (reactome, mean cos +0.57 to 40); *E2F G1/S* (control, mean cos +0.58 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +8.2 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +8.0 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.9 | +15.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.0 | +5.1 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.0 | +5.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.3 | +2.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.2 | +2.4 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.1 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -3.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.4 | -5.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -4.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.8 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.8 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -4.0 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | thyroid hormone receptor interactor 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:892,884-919,357 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 16E1BP |
| Gene groups (HGNC) | AAA ATPases |
| Hallmark sets | E2F_TARGETS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15645](https://www.uniprot.org/uniprotkb/Q15645) (Pachytene checkpoint protein 2 homolog):

> Plays a key role in chromosome recombination and chromosome structure development during meiosis. Required at early steps in meiotic recombination that leads to non-crossovers pathways. Also needed for efficient completion of homologous synapsis by influencing crossover distribution along the chromosomes affecting both crossovers and non-crossovers pathways. Also required for development of higher-order chromosome structures and is needed for synaptonemal-complex formation. In males, required …

**Summary**, from NCBI Gene [9319](https://www.ncbi.nlm.nih.gov/gene/9319):

> This gene encodes a protein that interacts with thyroid hormone receptors, also known as hormone-dependent transcription factors. The gene product interacts specifically with the ligand binding domain. This gene is one of several that may play a role in early-stage non-small cell lung cancer. [provided by RefSeq, Oct 2009]

**Accessions** — [HGNC:12307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12307) · Entrez [9319](https://www.ncbi.nlm.nih.gov/gene/9319) · UniProt [Q15645](https://www.uniprot.org/uniprotkb/Q15645) · Ensembl [ENSG00000071539](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000071539)

## Data

Gene col 986: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 986); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 986, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 986]; `tensor/DDL_lfc|DDL_z.npy` [986]; `embed/gene_vectors.npy` [986]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 986 or target_col == 986). Every well: [[TRIP13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRIP13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
