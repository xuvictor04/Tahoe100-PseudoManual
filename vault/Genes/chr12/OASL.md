---
symbol: "OASL"
type: "gene"
col: 5656
ensembl_id: "ENSG00000135114"
name: "2'-5'-oligoadenylate synthetase like"
location: "12q24.31"
module: 32
arm: "+"
pooled_cpm: 57.17
n_lines_expressing: 40
n_dd_up: 22
n_dd_down: 72
n_dd_up_clean: 21
n_dd_down_clean: 59
in_vector_space: true
direction_upstream: 46
direction_downstream: 57
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# OASL

*2'-5'-oligoadenylate synthetase like* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.58× (z +8.4, q 2e-14, up in 32 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 72 drug-doses (13 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.375× (z -12.4, q 2e-32, down in 32 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.92, fdr 7e-06), [[RIGI]] (+0.92, fdr 7e-06), [[IFIT1]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 46 arrows point to it, the strongest [[PLAAT4]] → it (grade B ⚠); 57 go from it, the strongest it → [[CASP10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.58×** | +8.4 | 2e-14 | 32/38 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.57×** | +8.1 | 1e-13 | 25/38 (NCI-H460, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.95×** | +6.0 | 4e-07 | 23/38 (NCI-H460, LS 180, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +5.5 | 5e-06 | 25/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.54×** | +5.4 | 6e-06 | 20/38 (NCI-H460, LS 180, …) | two highest doses | composition shift |
| [[venetoclax (drug)]] 0.05 µM |  | **1.75×** | +4.7 | 2e-04 | 32/39 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.003 | 19/38 (LoVo, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.005 | 16/38 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +3.8 | 0.008 | 19/39 (LS 180, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **1.56×** | +3.7 | 0.010 | 20/39 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.78×** | +3.7 | 0.013 | 18/38 (NCI-H1573, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.48×** | +3.5 | 0.019 | 18/38 (NCI-H1792, SNU-423, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.026 | 18/38 (AsPC-1, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.44×** | +3.1 | 0.068 | 17/38 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.068 | 17/38 (A-172, A498, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.068 | 13/37 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 72 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 72 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM |  | **0.375×** | -12.4 | 2e-32 | 32/38 (SNU-423, NCI-H1792, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.259×** | -12.1 | 5e-31 | 36/38 (LoVo, A498, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.276×** | -11.5 | 3e-28 | 27/39 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.474×** | -9.4 | 6e-19 | 25/39 (A549, MIA PaCa-2, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.341×** | -9.2 | 3e-18 | 25/36 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.373×** | -8.8 | 1e-16 | 28/38 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.499×** | -8.8 | 1e-16 | 35/39 (A-172, A498, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.376×** | -8.7 | 2e-16 | 29/38 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.394×** | -8.3 | 7e-15 | 29/38 (BT-474, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.402×** | -8.1 | 2e-14 | 28/38 (NCI-H1792, A549, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.530×** | -8.0 | 6e-14 | 24/39 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.418×** | -7.5 | 4e-12 | 22/29 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.433×** | -7.5 | 4e-12 | 32/38 (BT-474, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.439×** | -7.3 | 9e-12 | 24/38 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -7.1 | 5e-11 | 25/38 (COLO 205, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.459×** | -6.9 | 1e-10 | 28/38 (H4, A-172, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.469×** | -6.7 | 5e-10 | 24/38 (NCI-H1792, LoVo, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.469×** | -6.7 | 5e-10 | 21/38 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.468×** | -6.5 | 2e-09 | 25/37 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.482×** | -6.5 | 2e-09 | 30/38 (NCI-H1792, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 73.3 | 0 | 15 (4 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0365× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 74.6 | 0 | 15 (5 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.124× (z -15.5) |
| [[LoVo (line)]] | wt | 118 | 0 | 11 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0506× (z -18.6) |
| [[COLO 205 (line)]] | alt | 151 | 0 | 9 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0605× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 0.152× (z -12.3) |
| [[BT-474 (line)]] | alt | 38.6 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0211× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0895× (z -10.9) |
| [[MIA PaCa-2 (line)]] | alt | 72.4 | 0 | 7 (1 ⚠) | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0453× (z -13.9) |
| [[NCI-H2347 (line)]] | alt | 54.6 | 2 | 5 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 7.00× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.362× (z -9.3) |
| [[NCI-H460 (line)]] | wt | 244 | 5 (1 ⚠) | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 8.16× (z +14.6) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.148× (z -13.7) ⚠ unreliable plate only |
| [[A498 (line)]] | wt | 113 | 0 | 6 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0870× (z -14.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.129× (z -12.7) |
| [[LS 180 (line)]] | wt | 123 | 3 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +13.5) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.09× (z +10.0) | [[Auranofin (drug)]] 5 µM 0.245× (z -9.9) |
| [[NCI-H23 (line)]] | alt | 28.2 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -11.8) |
| [[CFPAC-1 (line)]] | alt | 55.0 | 1 | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 6.64× (z +9.7) | [[Tofacitinib (drug)]] 5 µM 0.205× (z -11.8) |
| [[H4 (line)]] | wt | 67.4 | 0 | 4 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0273× (z -13.4) ⚠ transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0959× (z -8.7) |
| [[HS-578T (line)]] | alt | 46.6 | 0 | 4 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.149× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 48.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0907× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.102× (z -11.5) |
| [[A-172 (line)]] | wt | 139 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0641× (z -12.0) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.235× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 63.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.167× (z -9.9) |
| [[SNU-423 (line)]] | alt | 38.3 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.0712× (z -17.5) |
| [[NCI-H1573 (line)]] | alt | 24.7 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.167× (z -11.9) |
| [[Panc 03.27 (line)]] | alt | 51.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.190× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 30.9 | 0 | 2 | — | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.158× (z -8.9) |
| [[HOP62 (line)]] | alt | 28.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +10.6) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 47.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.18× (z +10.4) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[KATO III (line)]] | alt | 50.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.128× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 45.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +8.8) ⚠ cell-cycle shift, explains ~36% of this change | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0409× (z -8.5) |
| [[A-427 (line)]] | wt | 5.52 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.55 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.18 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.1 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 51.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 194 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 53.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.70 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 76.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 81.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.17 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 5.60 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 964 |
| [[RIGI]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999 |
| [[IFIT1]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 968 |
| [[IFIT2]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 963 |
| [[IFIH1]] | +0.89 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 940 |
| [[HERC5]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 947 |
| [[RSAD2]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 977 |
| [[OAS1]] | +0.88 | +0.81 / +0.90 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 884 |
| [[OAS2]] | +0.88 | +0.83 / +0.88 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 884 |
| [[IFI44]] | +0.87 | +0.84 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 950 |
| [[DDX60]] | +0.87 | +0.81 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 888 |
| [[CMPK2]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 722 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 28, C 18. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAAT4]] | B | PLAAT4 activity raises OASL's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 3.22× lower at baseline in the lines without PLAAT4 | 2e-04 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[IFIT2]] | B | IFIT2 activity raises OASL's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 3.83× lower at baseline in the lines without IFIT2 | 0.005 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |
| [[IFIT3]] | B | IFIT3 activity raises OASL's level | lines that do not express IFIT3 (8) vs lines expressing it (42) | 3.83× lower at baseline in the lines without IFIT3 | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP2, IFIT2, TRIM38; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises OASL's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.26× lower at baseline in the lines without RSAD2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[EPSTI1]] | B | EPSTI1 activity raises OASL's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.80× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[CTSS]] | B | CTSS activity raises OASL's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.10× lower at baseline in the lines without CTSS | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[IFI44]] | B | IFI44 activity raises OASL's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.11× lower at baseline in the lines without IFI44 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[CASP10]] | B | CASP10 activity raises OASL's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 2.45× lower at baseline in the lines without CASP10 | 0.008 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[APOL1]] | B | APOL1 activity raises OASL's level | lines that do not express APOL1 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without APOL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: POU5F1, UGT1A6, NMRAL2P-1 |
| [[GBP1]] | B | GBP1 activity raises OASL's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without GBP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[GBP4]] | B | GBP4 activity raises OASL's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.66× lower at baseline in the lines without GBP4 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[APOL3]] | B | APOL3 activity raises OASL's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without APOL3 | 0.023 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 55, C 2. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP10]] | B | OASL activity raises CASP10's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.38× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[HLA-E]] | B | OASL activity raises HLA-E's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFIT3]] | B | OASL activity raises IFIT3's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.49× lower at baseline in the lines without OASL | 0.001 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFI44]] | B | OASL activity raises IFI44's level | lines that do not express OASL (10) vs lines expressing it (40) | 4.19× lower at baseline in the lines without OASL | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFIT2]] | B | OASL activity raises IFIT2's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.25× lower at baseline in the lines without OASL | 0.002 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[ZC3HAV1]] | B | OASL activity raises ZC3HAV1's level | lines that do not express OASL (10) vs lines expressing it (40) | 1.93× lower at baseline in the lines without OASL | 0.003 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[GBP1]] | B | OASL activity raises GBP1's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.85× lower at baseline in the lines without OASL | 0.004 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[GBP3]] | B | OASL activity raises GBP3's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.72× lower at baseline in the lines without OASL | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[IFIT1]] | B | OASL activity raises IFIT1's level | lines that do not express OASL (10) vs lines expressing it (40) | 2.98× lower at baseline in the lines without OASL | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[DDX60]] | B | OASL activity raises DDX60's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.07× lower at baseline in the lines without OASL | 0.006 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[HERC5]] | B | OASL activity raises HERC5's level | lines that do not express OASL (10) vs lines expressing it (40) | 4.74× lower at baseline in the lines without OASL | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |
| [[CTSS]] | B | OASL activity raises CTSS's level | lines that do not express OASL (10) vs lines expressing it (40) | 3.37× lower at baseline in the lines without OASL | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, GBP2, TENT5A; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.898). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.3, 53.1); signed map (64.5, 31.1). **Vector** length 158, 57.1% of its response variance represented; |z| ≥ 3 in 1,447 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.81 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.81 to 11); *IFIT antiviral response* (reactome, mean cos +0.87 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.0 | +8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +6.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +5.9 | +5.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +3.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.6 | +1.2 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.4 | +4.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.2 | +3.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.1 | +3.7 |
| fall | [[Selinexor (drug)]] 5 µM |  | -8.9 | -12.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -8.3 | -9.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -7.4 | -8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.4 | -8.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -7.2 | -8.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.0 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | 2'-5'-oligoadenylate synthetase like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,017,763-121,039,246 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRIP14, p59OASL, OASL1 |
| Gene groups (HGNC) | 2'-5'-oligoadenylate synthetase family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 6 pathways, smallest: OAS antiviral response; Interferon alpha/beta signaling; Interferon gamma signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15646](https://www.uniprot.org/uniprotkb/Q15646) (2'-5'-oligoadenylate synthase-like protein):

> Does not have 2'-5'-OAS activity, but can bind double-stranded RNA. Displays antiviral activity against encephalomyocarditis virus (EMCV) and hepatitis C virus (HCV) via an alternative antiviral pathway independent of RNase L.

**Summary**, from NCBI Gene [8638](https://www.ncbi.nlm.nih.gov/gene/8638):

> Enables DNA binding activity and double-stranded RNA binding activity. Involved in several processes, including interleukin-27-mediated signaling pathway; negative regulation of viral genome replication; and positive regulation of RIG-I signaling pathway. Located in cytosol and nucleolus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:8090](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8090) · Entrez [8638](https://www.ncbi.nlm.nih.gov/gene/8638) · UniProt [Q15646](https://www.uniprot.org/uniprotkb/Q15646) · Ensembl [ENSG00000135114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135114)

## Data

Gene col 5656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5656); `tables/drug_effects.parquet` (94 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5656]; `tensor/DDL_lfc|DDL_z.npy` [5656]; `embed/gene_vectors.npy` [5656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5656 or target_col == 5656). Every well: [[OASL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OASL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
