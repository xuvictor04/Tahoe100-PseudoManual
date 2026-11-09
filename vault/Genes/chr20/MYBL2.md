---
symbol: "MYBL2"
type: "gene"
col: 2065
ensembl_id: "ENSG00000101057"
name: "MYB proto-oncogene like 2"
location: "20q13.12"
module: 6
arm: "+"
pooled_cpm: 20.38
n_lines_expressing: 46
n_dd_up: 35
n_dd_down: 25
n_dd_up_clean: 6
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 11
direction_downstream: 65
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MYBL2

*MYB proto-oncogene like 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (29 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.71× (z +16.5, q 0e+00, up in 35 of 36 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change. The strongest without an alert is [[Retinoic acid (drug)]] 0.05 µM: 1.41× (z +3.6, q 0.007, up in 11 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.551× (z -6.4, q 9e-08, down in 27 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR76]] (+0.93, fdr 7e-06), [[POLE]] (+0.90, fdr 7e-06), [[EXO1]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 65 go from it, the strongest it → [[POLQ]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 29 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 29 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **4.71×** | +16.5 | 0e+00 | 35/36 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | **4.39×** | +15.2 | 0e+00 | 23/24 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **2.83×** | +10.3 | 2e-22 | 30/34 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~64% of this change | **1.89×** | +6.5 | 1e-08 | 23/40 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.82×** | +6.4 | 2e-08 | 25/43 (SW480, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.81×** | +6.3 | 2e-08 | 25/43 (SW1417, A549, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.78×** | +6.1 | 7e-08 | 21/44 (SW1417, A549, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.45×** | +5.6 | 1e-06 | 21/42 (A549, NCI-H2030, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.67×** | +5.5 | 3e-06 | 22/44 (SW480, J82, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.66×** | +5.4 | 4e-06 | 21/44 (SW1417, NCI-H460, …) | rises with dose | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **1.40×** | +5.1 | 2e-05 | 25/44 (HT-29, SW480, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.61×** | +5.1 | 2e-05 | 26/43 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.64×** | +5.0 | 2e-05 | 25/42 (SW480, HCT15, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.60×** | +4.8 | 6e-05 | 21/41 (SW480, PANC-1, …) | rises with dose | position effect removed |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.57×** | +4.8 | 7e-05 | 25/44 (SW480, HCT15, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.007 | 11/44 (MIA PaCa-2, A498, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.016 | 9/43 (SW480, CFPAC-1, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.22×** | +2.9 | 0.060 | 16/44 (SW480, J82, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.33×** | +2.8 | 0.083 | 9/43 (A-427, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +2.8 | 0.086 | 10/44 (SW480, SNU-423, …) | rises with dose | position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.65×** | +2.8 | 0.089 | 7/41 (NCI-H460, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.551×** | -6.4 | 9e-08 | 27/42 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.597×** | -5.5 | 9e-06 | 25/43 (A498, A-172, …) | all doses, stronger at high dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.496×** | -5.4 | 2e-05 | 23/44 (HT-29, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | **0.706×** | -5.3 | 2e-05 | 24/44 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.715×** | -5.1 | 4e-05 | 24/44 (A498, A-427, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.763×** | -4.1 | 0.004 | 22/44 (Panc 03.27, NCI-H23, …) | rises with dose | position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.593×** | -4.0 | 0.005 | 20/44 (Hs 766T, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.690×** | -4.0 | 0.005 | 17/44 (NCI-H23, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.693×** | -3.9 | 0.005 | 25/41 (H4, RKO, …) | rises with dose | position effect removed |
| [[4EGI-1 (drug)]] 5 µM |  | **0.496×** | -3.9 | 0.005 | 21/41 (Panc 03.27, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.681×** | -3.9 | 0.005 | 19/44 (RPMI-7951, MIA PaCa-2, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.624×** | -3.6 | 0.014 | 11/44 (LoVo, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.715×** | -3.6 | 0.014 | 16/42 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.791×** | -3.6 | 0.014 | 18/44 (J82, SHP-77, …) | all doses, stronger at high dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.713×** | -3.4 | 0.023 | 19/42 (A-172, HCT15, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 5 µM |  | **0.554×** | -3.3 | 0.030 | 19/41 (SW480, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[BAY1125976 (drug)]] 5 µM |  | **0.556×** | -3.3 | 0.030 | 14/44 (MIA PaCa-2, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.814×** | -3.1 | 0.045 | 15/44 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.736×** | -3.1 | 0.046 | 18/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Terfenadine (drug)]] 5 µM |  | **0.816×** | -3.1 | 0.046 | 14/44 (SW 1271, A-427, …) | top dose only | position effect removed |
| [[Sapanisertib (drug)]] 5 µM |  | **0.589×** | -3.0 | 0.068 | 9/44 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.50 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 31.4 | 2 (2 ⚠) | 5 (4 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.56× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | [[Selinexor (drug)]] 5 µM 0.218× (z -15.0) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Amsacrine (drug)]] 5 µM 0.388× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 28.0 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 6.42× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -14.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0921× (z -12.6) |
| [[SW480 (line)]] | alt | 21.0 | 5 (5 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 4.78× (z +11.4) ⚠ toxic; cell-cycle shift, would explain all of this change | — |
| [[NCI-H460 (line)]] | wt | 14.0 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 5 µM 7.05× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | [[Selinexor (drug)]] 0.5 µM 0.163× (z -10.4) ⚠ cell-cycle shift, explains ~66% of this change |
| [[A-427 (line)]] | wt | 48.6 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.292× (z -11.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.295× (z -11.8) |
| [[H4 (line)]] | wt | 15.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0459× (z -11.5) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Temsirolimus (drug)]] 0.5 µM 0.0922× (z -8.9) |
| [[LS 180 (line)]] | wt | 13.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.46× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.152× (z -10.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0927× (z -9.6) |
| [[PANC-1 (line)]] | alt | 21.3 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.22× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | — |
| [[A-172 (line)]] | wt | 28.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.238× (z -11.6) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HEC-1-A (line)]] | alt | 40.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.213× (z -11.3) |
| [[LoVo (line)]] | wt | 11.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 0.5 µM 0.172× (z -9.1) ⚠ cell-cycle shift, explains ~66% of this change |
| [[Panc 03.27 (line)]] | alt | 19.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.94× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | [[Selinexor (drug)]] 5 µM 0.240× (z -10.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[A549 (line)]] | wt | 9.88 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.72× (z +9.0) ⚠ cell-cycle shift, explains ~96% of this change | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 1 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0916× (z -9.6) |
| [[HCT15 (line)]] | alt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.28× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[LOX-IMVI (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.196× (z -10.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[NCI-H23 (line)]] | alt | 42.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -8.7) |
| [[SW1417 (line)]] | alt | 37.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | — |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 63.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.67 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR76]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[POLE]] | +0.90 | +0.90 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[EXO1]] | +0.90 | +0.91 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 633 |
| [[MCM4]] | +0.90 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 533 |
| [[CLSPN]] | +0.89 | +0.86 / +0.88 | both halves | 7e-06 | STRING 411 |
| [[XRCC2]] | +0.88 | +0.85 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[CDC45]] | +0.88 | +0.88 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 693 |
| [[CENPK]] | +0.88 | +0.85 / +0.90 | both halves | 7e-06 |  |
| [[NCAPG2]] | +0.88 | +0.88 / +0.88 | both halves | 7e-06 | **novel candidate** |
| [[HELLS]] | +0.88 | +0.84 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[PCLAF]] | +0.87 | +0.87 / +0.87 | both halves | 7e-06 |  |
| [[MELK]] | +0.87 | +0.86 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 894 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 5, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYBL2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 6.2% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises MYBL2's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without FAM111B | 0.046 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MYBL2's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.08× lower at baseline in the lines without E2F2 | 0.081 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises MYBL2's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.14× lower at baseline in the lines without CDCA7 | 0.083 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises MYBL2's level | compounds that target MTOR: 4 of 8 lower it (AZD-8055, Rapamycin, Sapanisertib, Temsirolimus) | 50% of the class's compounds vs 4.8% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDC25A]] | C | CDC25A activity raises MYBL2's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.70× lower at baseline in the lines without CDC25A | 0.031 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent; co-absent with the target |
| [[TCF19]] | C | TCF19 activity raises MYBL2's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.75× lower at baseline in the lines without TCF19 | 0.056 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[E2F8]] | C | E2F8 activity raises MYBL2's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.72× lower at baseline in the lines without E2F8 | 0.064 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent; co-absent with the target |
| [[DSCC1]] | C | DSCC1 activity raises MYBL2's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.70× lower at baseline in the lines without DSCC1 | 0.082 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[SHMT1]] | C | SHMT1 activity raises MYBL2's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.32× lower at baseline in the lines without SHMT1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; its own permutation p |
| [[BRME1]] | C | BRME1 activity raises MYBL2's level | lines that do not express BRME1 (4) vs lines expressing it (46) | 2.44× lower at baseline in the lines without BRME1 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: FOXRED2, NRTN, TENT5C; maybe low, not absent |

### Downstream of this gene

*65 arrows, 65 of them with an alert ⚠; grade A 0, B 0, C 65. Shown: the 12 strongest; 53 more arrows (53 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[POLQ]] | C | MYBL2 activity raises POLQ's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.46× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[XRCC2]] | C | MYBL2 activity raises XRCC2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.28× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[LMNB1]] | C | MYBL2 activity raises LMNB1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.22× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[GINS1]] | C | MYBL2 activity raises GINS1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.16× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[FANCD2]] | C | MYBL2 activity raises FANCD2's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.10× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[BLM]] | C | MYBL2 activity raises BLM's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 3.09× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[SKA3]] | C | MYBL2 activity raises SKA3's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[RAD51AP1]] | C | MYBL2 activity raises RAD51AP1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.93× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[PCLAF]] | C | MYBL2 activity raises PCLAF's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.87× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; co-absent with the target; its own permutation p |
| [[ATAD5]] | C | MYBL2 activity raises ATAD5's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.80× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[RBL1]] | C | MYBL2 activity raises RBL1's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.77× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |
| [[ASF1B]] | C | MYBL2 activity raises ASF1B's level | lines that do not express MYBL2 (4) vs lines expressing it (46) | 2.71× lower at baseline in the lines without MYBL2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SMARCD3, DNMT3B, DSCC1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.941). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.6, -44.4); signed map (-37.7, -45.8). **Vector** length 132, 41.3% of its response variance represented; |z| ≥ 3 in 1,216 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA strand elongation* (reactome, mean cos +0.75 to 28); *DNA Replication* (reactome, mean cos +0.74 to 40); *E2F G1/S* (control, mean cos +0.75 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change | +8.3 | +15.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +7.9 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | +7.8 | +16.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | +6.1 | +6.4 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | +4.6 | +4.7 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.0 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.4 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.7 | +2.7 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.7 | +2.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.5 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | -5.2 | -5.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -5.1 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~55% of this change | -4.0 | -3.4 |
|  | [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~65% of this change | -3.8 | -5.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.2 | -1.1 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.0 | -2.8 |
|  | [[Temsirolimus (drug)]] 5 µM |  | -2.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | MYB proto-oncogene like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:43,667,019-43,716,495 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BMYB, B-MYB |
| Gene groups (HGNC) | Myb/SANT domain containing; MMB complex subunits |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 10 pathways, smallest: TFAP2A acts as a transcriptional repressor during retinoic acid induced cell differentiation; Polo-like kinase mediated events; Transcription of E2F targets under negative control by p107 (RBL1) and p130 (RBL2) in complex with HDAC1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P10244](https://www.uniprot.org/uniprotkb/P10244) (Myb-related protein B):

> Transcription factor involved in the regulation of cell survival, proliferation, and differentiation. Transactivates the expression of the CLU gene.

**Summary**, from NCBI Gene [4605](https://www.ncbi.nlm.nih.gov/gene/4605):

> The protein encoded by this gene, a member of the MYB family of transcription factor genes, is a nuclear protein involved in cell cycle progression. The encoded protein is phosphorylated by cyclin A/cyclin-dependent kinase 2 during the S-phase of the cell cycle and possesses both activator and repressor activities. It has been shown to activate the cell division cycle 2, cyclin D1, and insulin-like growth factor-binding protein 5 genes. Two transcript variants encoding different isoforms have …

**Accessions** — [HGNC:7548](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7548) · Entrez [4605](https://www.ncbi.nlm.nih.gov/gene/4605) · UniProt [P10244](https://www.uniprot.org/uniprotkb/P10244) · Ensembl [ENSG00000101057](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101057)

## Data

Gene col 2065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2065); `tables/drug_effects.parquet` (60 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2065]; `tensor/DDL_lfc|DDL_z.npy` [2065]; `embed/gene_vectors.npy` [2065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2065 or target_col == 2065). Every well: [[MYBL2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYBL2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
