---
symbol: "CDON"
type: "gene"
col: 743
ensembl_id: "ENSG00000064309"
name: "cell adhesion associated, oncogene regulated"
location: "11q24.2"
module: 99
arm: "+"
pooled_cpm: 28.81
n_lines_expressing: 47
n_dd_up: 23
n_dd_down: 49
n_dd_up_clean: 22
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/099"]
generated_by: "tahoemap"
---

# CDON

*cell adhesion associated, oncogene regulated* — 11q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.19× (z +17.2, q 0e+00, up in 39 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.361× (z -20.7, q 0e+00, down in 40 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDK3]] (+0.80, fdr 7e-06), [[TPD52]] (+0.76, fdr 7e-06), [[HACE1]] (+0.76, fdr 7e-06); moves opposite to [[CFLAR]] (-0.73, fdr 7e-06), [[ITPA]] (-0.72, fdr 7e-06), [[SPRY3]] (-0.70, fdr 3e-05).
> It is in [[Module 099]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); 6 go from it, the strongest it → [[ATP6V0E2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 743.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.19×** | +17.2 | 0e+00 | 39/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.63×** | +14.4 | 3e-44 | 38/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.59×** | +14.1 | 8e-43 | 37/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.90×** | +13.2 | 2e-37 | 39/45 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.25×** | +12.0 | 3e-31 | 36/45 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.11×** | +11.1 | 2e-26 | 37/45 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.19×** | +9.0 | 2e-17 | 38/45 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.59×** | +6.6 | 2e-09 | 28/44 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 24/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +4.7 | 2e-04 | 18/43 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 2e-04 | 20/44 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 3e-04 | 19/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.29×** | +4.4 | 5e-04 | 22/45 (SW480, HOP62, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.36×** | +4.2 | 0.001 | 13/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.22×** | +4.1 | 0.001 | 17/45 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.1 | 0.002 | 14/45 (SW480, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 743.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.361×** | -20.7 | 0e+00 | 40/44 (HS-578T, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.275×** | -19.2 | 0e+00 | 42/44 (SK-MEL-2, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.263×** | -19.2 | 0e+00 | 41/44 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.336×** | -16.3 | 0e+00 | 42/45 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.362×** | -15.1 | 0e+00 | 40/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.373×** | -14.7 | 0e+00 | 40/44 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.436×** | -12.4 | 3e-33 | 38/44 (LS 180, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.437×** | -12.3 | 4e-33 | 41/45 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.430×** | -12.1 | 7e-32 | 23/33 (HEC-1-A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.522×** | -9.3 | 7e-19 | 35/43 (RPMI-7951, NCI-H460, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.540×** | -9.2 | 2e-18 | 28/40 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.603×** | -7.6 | 2e-12 | 30/45 (HS-578T, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.705×** | -7.3 | 1e-11 | 30/45 (SNU-1, PANC-1, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -7.0 | 1e-10 | 29/45 (HT-29, NCI-H460, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.611×** | -6.8 | 4e-10 | 25/39 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.637×** | -6.7 | 6e-10 | 28/45 (NCI-H460, A498, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.645×** | -6.6 | 2e-09 | 24/45 (NCI-H460, HS-578T, …) | two highest doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.686×** | -5.6 | 5e-07 | 23/44 (NCI-H460, SNU-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.673×** | -5.6 | 6e-07 | 22/44 (A498, SW480, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.500×** | -5.4 | 2e-06 | 22/44 (LS 180, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 743. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.8 | 0 | 14 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0524× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.114× (z -14.9) |
| [[PANC-1 (line)]] | alt | 27.5 | 3 | 9 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 5.78× (z +14.6) | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -14.3) |
| [[SW480 (line)]] | alt | 18.2 | 5 | 6 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 6.26× (z +15.0) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.142× (z -15.9) |
| [[HS-578T (line)]] | alt | 103 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0710× (z -24.3) |
| [[LoVo (line)]] | wt | 21.5 | 2 | 8 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.38× (z +9.7) | [[Digitoxin (drug)]] 5 µM 0.0687× (z -21.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.148× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 125 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0340× (z -18.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0335× (z -18.2) |
| [[SW1417 (line)]] | alt | 21.4 | 3 | 7 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.94× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -14.4) |
| [[HT-29 (line)]] | alt | 44.0 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.186× (z -16.6) |
| [[SNU-1 (line)]] | wt | 41.5 | 0 | 9 (4 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0608× (z -15.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 33.2 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0834× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.214× (z -17.3) |
| [[A498 (line)]] | wt | 12.0 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0750× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.160× (z -14.9) |
| [[KATO III (line)]] | alt | 24.8 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.46× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.142× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -14.1) |
| [[NCI-H1573 (line)]] | alt | 22.0 | 3 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.19× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.179× (z -10.0) |
| [[A-172 (line)]] | wt | 43.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -16.5) |
| [[CFPAC-1 (line)]] | alt | 23.6 | 2 | 3 | [[Panobinostat (drug)]] 5 µM 4.51× (z +8.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 52.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -15.4) |
| [[C32 (line)]] | wt | 34.7 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -12.9) |
| [[CHP-212 (line)]] | wt | 115 | 0 | 4 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.148× (z -11.6) |
| [[LOX-IMVI (line)]] | wt | 14.5 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 4.12× (z +8.5) | [[Harringtonine (drug)]] 5 µM 0.0953× (z -13.5) |
| [[NCI-H23 (line)]] | alt | 29.1 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -16.8) |
| [[Panc 03.27 (line)]] | alt | 31.4 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.229× (z -9.9) |
| [[SHP-77 (line)]] | alt | 103 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0768× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -14.1) |
| [[A-427 (line)]] | wt | 31.2 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.156× (z -13.8) |
| [[A549 (line)]] | wt | 13.7 | 1 | 2 | [[Panobinostat (drug)]] 5 µM 5.06× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -12.4) |
| [[HOP62 (line)]] | alt | 63.1 | 1 (1 ⚠) | 2 | [[Adagrasib (drug)]] 0.05 µM 2.39× (z +13.9) ⚠ position not correctable | [[Harringtonine (drug)]] 5 µM 0.0773× (z -11.4) |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0711× (z -13.3) |
| [[SW 900 (line)]] | alt | 41.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0521× (z -23.7) |
| [[H4 (line)]] | wt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0978× (z -10.4) |
| [[HCT15 (line)]] | alt | 27.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.171× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[Hs 766T (line)]] | wt | 8.94 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.113× (z -9.1) |
| [[J82 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -10.5) |
| [[MIA PaCa-2 (line)]] | alt | 13.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.98× (z +11.0) ⚠ position not correctable | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~56% of this change |
| [[NCI-H2347 (line)]] | alt | 7.40 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.35× (z +8.8) | — |
| [[SW48 (line)]] | wt | 22.8 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.112× (z -9.8) |
| [[C-33 A (line)]] | alt | 84.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 20.1 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.182× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 20.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0340× (z -18.9) |
| [[AN3 CA (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.03 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.77 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.94 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 743), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDK3]] | +0.80 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[TPD52]] | +0.76 | +0.71 / +0.61 | both halves | 7e-06 |  |
| [[HACE1]] | +0.76 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[ARL6]] | +0.75 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[RAB3A]] | +0.73 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.72 | +0.73 / +0.50 | both halves | 1e-05 |  |
| [[SNAPC3]] | +0.71 | +0.68 / +0.51 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.71 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PFKFB4]] | +0.70 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[GPR160]] | +0.70 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ARL3]] | +0.69 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[UBE2Q2P2]] | +0.69 | +0.62 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFLAR]] | -0.73 | -0.63 / -0.62 | both halves | 7e-06 |  |
| [[ITPA]] | -0.72 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[SPRY3]] | -0.70 | -0.63 / -0.46 | both halves | 3e-05 |  |
| [[ST7L]] | -0.70 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ITPRIPL2]] | -0.68 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[WARS2-AS1]] | -0.68 | -0.61 / -0.40 | both halves | 4e-05 |  |
| [[DPH5-DT]] | -0.67 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[PPP3CB-AS1]] | -0.67 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.67 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[MCPH1]] | -0.66 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[MMADHC-DT]] | -0.65 | -0.56 / -0.33 | both halves | 1e-04 |  |
| [[INO80D]] | -0.65 | -0.48 / -0.54 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 5, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers CDON's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 2.8% of all compounds | 0.053 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[ROR2]] | B | ROR2 activity raises CDON's level | lines that do not express ROR2 (25) vs lines expressing it (25) | 1.51× lower at baseline in the lines without ROR2 | 0.069 | ⚠ within organs, on part of the lines; also absent: BEGAIN, OLFM1, HOXD11 |
| [[ZNF331]] | B | ZNF331 activity raises CDON's level | lines that do not express ZNF331 (15) vs lines expressing it (35) | 1.71× lower at baseline in the lines without ZNF331 | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF256, SNRPN, ZNF625 |
| [[TOP2A]] | B | TOP2A activity raises CDON's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.7% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CREB3L1]] | B | CREB3L1 activity weakens CDON's drug response | lines that do not express CREB3L1 (23) vs lines expressing it (22) | the lines without CREB3L1 respond 1.25× as strongly (z diff -1.22); strongest at Panobinostat 0.5 µM: 2.84x vs 2.18x (z diff -2.4) | 0.089 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1; target measured in part of the lines; artifact flags |
| [[SH3D19]] | C | SH3D19 activity lowers CDON's level | lines that do not express SH3D19 (3) vs lines expressing it (47) | 4.16× higher at baseline in the lines without SH3D19 | 0.016 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1, APOBEC3B; maybe low, not absent |
| [[ATP6V0E2]] | C | ATP6V0E2 activity raises CDON's level | lines that do not express ATP6V0E2 (5) vs lines expressing it (45) | 2.37× lower at baseline in the lines without ATP6V0E2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CDON, ODAD4; co-absent with the target |
| [[RFX3-DT]] | C | RFX3-DT activity raises CDON's level | lines that do not express RFX3-DT (3) vs lines expressing it (47) | 2.51× lower at baseline in the lines without RFX3-DT | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: POGLUT2, ANAPC1P4, WDR35; maybe low, not absent; its own permutation p |
| [[SH3D19]] | C | SH3D19 activity strengthens CDON's drug response | lines that do not express SH3D19 (3) vs lines expressing it (42) | the lines without SH3D19 respond 0.55× as strongly (z diff +2.59); strongest at Panobinostat 5 µM: 1.22x vs 3.17x (z diff +5.2) | 0.096 | ⚠ few lines (3 vs 47); across organs; also absent: HPS1, APOBEC3B; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP6V0E2]] | C | CDON activity raises ATP6V0E2's level | lines that do not express CDON (3) vs lines expressing it (47) | 3.94× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; co-absent with the target; its own permutation p |
| [[MLF1]] | C | CDON activity raises MLF1's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |
| [[PPP3CB-AS1]] | C | CDON activity raises PPP3CB-AS1's level | lines that do not express CDON (3) vs lines expressing it (47) | 1.12× lower at baseline in the lines without CDON | 0.062 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |
| [[ACO1]] | C | CDON activity lowers ACO1's level | lines that do not express CDON (3) vs lines expressing it (47) | 1.60× higher at baseline in the lines without CDON | 0.078 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent |
| [[GPI]] | C | CDON activity raises GPI's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.33× lower at baseline in the lines without CDON | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |
| [[DDIT4]] | C | CDON activity raises DDIT4's level | lines that do not express CDON (3) vs lines expressing it (47) | 2.17× lower at baseline in the lines without CDON | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: ATP6V0E2, DBNDD1, NAT14; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 099]] — hypoxia; 48 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.7, -12.1); signed map (-31.9, 21.5). **Vector** length 106, 31.0% of its response variance represented; |z| ≥ 3 in 1,622 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.53 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.6 | +13.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +6.2 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.9 | +11.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.5 | +14.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.1 | +14.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.8 | +9.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +5.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -7.2 | -19.2 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.6 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.1 | -19.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.5 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -20.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -6.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.8 | -1.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -4.8 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.4 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cell adhesion associated, oncogene regulated |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q24.2 — chr11:125,955,796-126,063,335 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ORCAM, CDO, CDON1, Ihog |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing |
| Hallmark sets | UV_RESPONSE_DN |
| Reactome | 5 pathways, smallest: Ligand-receptor interactions; Activation of SMO; Myogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4KMG0](https://www.uniprot.org/uniprotkb/Q4KMG0) (Cell adhesion molecule-related/down-regulated by oncogenes):

> Together with BOC, forms a coreceptor required for sonic hedgehog (SHH) handoff to its patched receptor (PTCH1 or PTCH2), thereby allowing activation of the smoothened signaling pathway (By similarity). Binds to the dually lipid-modified Sonic hedgehog protein N-product (ShhN) downstream of SCUBE2 carrier and promotes its release to GAS1 (By similarity). ShhN is then directly transferred to patched receptor by GAS1 (By similarity). May also mediate cell-cell interactions between muscle …

**Summary**, from NCBI Gene [50937](https://www.ncbi.nlm.nih.gov/gene/50937):

> This gene encodes a cell surface receptor that is a member of the immunoglobulin superfamily. The encoded protein contains three fibronectin type III domains and five immunoglobulin-like C2-type domains. This protein is a member of a cell-surface receptor complex that mediates cell-cell interactions between muscle precursor cells and positively regulates myogenesis. [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:17104](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17104) · Entrez [50937](https://www.ncbi.nlm.nih.gov/gene/50937) · UniProt [Q4KMG0](https://www.uniprot.org/uniprotkb/Q4KMG0) · Ensembl [ENSG00000064309](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000064309)

## Data

Gene col 743: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 743); `tables/drug_effects.parquet` (75 rows, flagged included); `relations/gene_relations.parquet` (col_a == 743, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 743]; `tensor/DDL_lfc|DDL_z.npy` [743]; `embed/gene_vectors.npy` [743]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 743 or target_col == 743). Every well: [[CDON — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDON.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
