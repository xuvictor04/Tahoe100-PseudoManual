---
symbol: "RMND5B"
type: "gene"
col: 7042
ensembl_id: "ENSG00000145916"
name: "required for meiotic nuclear division 5 homolog B"
location: "5q35.3"
module: 129
arm: "+"
pooled_cpm: 19.31
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/129"]
generated_by: "tahoemap"
---

# RMND5B

*required for meiotic nuclear division 5 homolog B* — 5q35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.57× (z +8.9, q 2e-16, up in 29 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.37× (z +8.9, q 2e-16, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.613× (z -9.7, q 1e-19, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE2J2]] (+0.56, fdr 1e-05), [[FAM118B]] (+0.56, fdr 1e-05), [[BTBD10]] (+0.54, fdr 4e-05); moves opposite to [[BCO2]] (-0.60, fdr 3e-05), [[LAMP2]] (-0.52, fdr 1e-05), [[CREG1]] (-0.49, fdr 5e-05).
> It is in [[Module 129]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[WDR25]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 12 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7042.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.57×** | +8.9 | 2e-16 | 29/48 (LOX-IMVI, LS 180, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.37×** | +8.9 | 2e-16 | 25/47 (MIA PaCa-2, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.46×** | +7.5 | 1e-11 | 24/47 (CFPAC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.30×** | +5.2 | 3e-05 | 20/47 (H4, AsPC-1, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | **1.26×** | +4.5 | 9e-04 | 18/43 (AsPC-1, LS 180, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.25×** | +4.4 | 0.001 | 14/47 (COLO 205, A-172, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.0 | 0.005 | 10/48 (NCI-H23, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.25×** | +3.8 | 0.010 | 10/48 (CFPAC-1, HOP62, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.21×** | +3.7 | 0.011 | 13/47 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.21×** | +3.7 | 0.011 | 17/47 (LS 180, HEC-1-A, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.22×** | +3.7 | 0.011 | 8/48 (COLO 205, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.21×** | +3.6 | 0.016 | 17/47 (A498, A549, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.20× | +3.6 | 0.016 | 10/47 (SW 900, PANC-1, …) | rises with dose |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.19× | +3.5 | 0.020 | 8/47 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.19× | +3.4 | 0.024 | 11/47 (A549, A498, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.029 | 6/47 (SW 900, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.34×** | +3.1 | 0.070 | 1/48 (PANC-1) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 1.16× | +3.0 | 0.089 | 5/47 (NCI-H460, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7042.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.613×** | -9.7 | 1e-19 | 31/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.688×** | -7.4 | 3e-11 | 27/47 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.778×** | -7.1 | 3e-10 | 25/48 (SHP-77, KATO III, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.708×** | -6.9 | 8e-10 | 30/47 (NCI-H460, SW480, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.728×** | -6.3 | 3e-08 | 23/47 (AN3 CA, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.733×** | -5.9 | 3e-07 | 22/45 (BT-474, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.735×** | -5.9 | 3e-07 | 19/31 (LoVo, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | **0.808×** | -4.2 | 0.002 | 18/47 (NCI-H460, LS 180, …) | all doses, stronger at high dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.693×** | -3.8 | 0.009 | 10/45 (HT-29, AN3 CA, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.803×** | -3.7 | 0.013 | 8/48 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.833×** | -3.6 | 0.014 | 12/48 (NCI-H1573, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Gefitinib (drug)]] 5 µM |  | 0.849× | -3.3 | 0.051 | 4/48 (NCI-H460, NCI-H2030, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 0.898× | -3.0 | 0.10 | 13/48 (SHP-77, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7042. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.4 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.4) | [[Digitoxin (drug)]] 5 µM 0.328× (z -11.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.329× (z -11.0) |
| [[KATO III (line)]] | alt | 17.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[LoVo (line)]] | wt | 26.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.334× (z -10.2) |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -12.0) ⚠ toxic |
| [[A-427 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[BT-474 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.115× (z -14.1) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.167× (z -9.6) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 14.9 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.129× (z -8.7) |
| [[HT-29 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.237× (z -11.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.0) | — |
| [[NCI-H1573 (line)]] | alt | 27.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0871× (z -21.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 33.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.318× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[PANC-1 (line)]] | alt | 17.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +10.7) | — |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 20.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.142× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~56% of this change |
| [[SNU-423 (line)]] | alt | 9.67 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0950× (z -11.5) |
| [[SW1417 (line)]] | alt | 25.5 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.459× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 14.2 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.0851× (z -9.2) |
| [[SW480 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.348× (z -9.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.97 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7042), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE2J2]] | +0.56 | +0.61 / +0.49 | both halves | 1e-05 |  |
| [[FAM118B]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[BTBD10]] | +0.54 | +0.42 / +0.52 | both halves | 4e-05 |  |
| [[SLC12A4]] | +0.53 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ADRM1]] | +0.53 | +0.65 / +0.40 | both halves | 5e-05 |  |
| [[RNF34]] | +0.53 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[USP4]] | +0.53 | +0.40 / +0.48 | both halves | 4e-05 |  |
| [[ZGPAT]] | +0.53 | +0.47 / +0.44 | both halves | 3e-05 |  |
| [[RFFL]] | +0.53 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[NACC1]] | +0.52 | +0.62 / +0.37 | both halves | 8e-05 |  |
| [[ZNF767P-1]] | +0.52 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[BCAN-AS2]] | +0.51 | +0.59 / +0.33 | both halves | 1e-04 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BCO2]] | -0.60 | -0.47 / -0.45 | both halves | 3e-05 |  |
| [[LAMP2]] | -0.52 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[CREG1]] | -0.49 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[TMEM123]] | -0.48 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[LSMEM1]] | -0.47 | -0.23 / -0.53 | both halves | 5e-04 |  |
| [[SNX27]] | -0.46 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[STAG2]] | -0.45 | -0.39 / -0.50 | both halves | 5e-05 |  |
| [[SH3BGRL]] | -0.45 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[RIDA]] | -0.44 | -0.26 / -0.27 | both halves | 4e-04 |  |
| [[CXADR]] | -0.43 | -0.45 / -0.31 | both halves | 2e-04 |  |
| [[PEBP1]] | -0.43 | -0.45 / -0.36 | both halves | 1e-04 |  |
| [[TXNDC16]] | -0.43 | -0.42 / -0.19 | ⚠ not reproduced | 8e-04 |  |
| [[MBNL1]] | -0.43 | -0.45 / -0.32 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WDR25]] | C | WDR25's natural level strengthens RMND5B's drug response | WDR25's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse -0.33; direction not clear | 0.070 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 129]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.320). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-49.1, 2.7); signed map (-12.0, -22.3). **Vector** length 73.4, 12.3% of its response variance represented; |z| ≥ 3 in 860 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +3.8 | +8.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +2.8 | +4.4 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.7 | +3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~56% of this change | +2.5 | +4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.6 | +1.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.5 | +2.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.3 | -7.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -5.9 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -3.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -6.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.0 | -9.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -1.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | required for meiotic nuclear division 5 homolog B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.3 — chr5:178,130,996-178,150,568 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22318, GID2, GID2B |
| Gene groups (HGNC) | CTLH complex subunits; Degenerate RING E3 ubiquitin ligases |
| Reactome | 3 pathways, smallest: Regulation of pyruvate metabolism; Pyruvate metabolism; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96G75](https://www.uniprot.org/uniprotkb/Q96G75) (E3 ubiquitin-protein transferase RMND5B):

> Core component of the CTLH E3 ubiquitin-protein ligase complex that selectively accepts ubiquitin from UBE2H and mediates ubiquitination and subsequent proteasomal degradation of the transcription factor HBP1. MAEA and RMND5A are both required for catalytic activity of the CTLH E3 ubiquitin-protein ligase complex. Catalytic activity of the complex is required for normal cell proliferation. The CTLH E3 ubiquitin-protein ligase complex is not required for the degradation of enzymes involved in …

**Summary**, from NCBI Gene [64777](https://www.ncbi.nlm.nih.gov/gene/64777):

> Predicted to enable ubiquitin protein ligase activity and zinc ion binding activity. Predicted to contribute to ubiquitin-protein transferase activity. Predicted to be involved in proteasome-mediated ubiquitin-dependent protein catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26181](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26181) · Entrez [64777](https://www.ncbi.nlm.nih.gov/gene/64777) · UniProt [Q96G75](https://www.uniprot.org/uniprotkb/Q96G75) · Ensembl [ENSG00000145916](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145916)

## Data

Gene col 7042: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7042); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7042, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7042]; `tensor/DDL_lfc|DDL_z.npy` [7042]; `embed/gene_vectors.npy` [7042]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7042 or target_col == 7042). Every well: [[RMND5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RMND5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
