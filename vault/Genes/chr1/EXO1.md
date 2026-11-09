---
symbol: "EXO1"
type: "gene"
col: 10487
ensembl_id: "ENSG00000174371"
name: "exonuclease 1"
location: "1q43"
module: 6
arm: "+"
pooled_cpm: 27.71
n_lines_expressing: 48
n_dd_up: 40
n_dd_down: 42
n_dd_up_clean: 14
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 15
direction_downstream: 0
tags: ["gene", "module/006", "written"]
generated_by: "tahoemap"
---

# EXO1

*exonuclease 1* — 1q43

> [!summary] In one line
> EXO1 is a 5'-to-3' exonuclease that trims DNA ends in mismatch repair, long-range double-strand break resection and telomere processing.

## What it is

EXO1 is a Rad2/XPG-family nuclease, first identified in yeast as an exonuclease binding MSH2. In mismatch repair it degrades the error-containing strand from a nick after MutS and MutL license repair. In break repair it performs long-range resection, extending the 3' tail that RPA and then RAD51 occupy — the step committing a break to recombination; a DNA2-dependent route runs in parallel, both fed by BLM. Resection is actively blocked by [[TP53BP1]] with RIF1 and shieldin, which is how pathway choice is enforced. Expression is cell-cycle periodic under E2F and DREAM control, peaking in S phase; CDK phosphorylation adds another layer. Mouse knockouts are mismatch-repair deficient and tumour prone.

## What is uncertain

Direct repression by p53 is doubtful; the p21-relayed account fits better. Being a p53-repressed gene, its sign must be flipped before a change in it says anything about p53 output: a fall is the p53-active direction. Transcript level is a weak proxy for resection capacity, and a modest fall at 24 h is as consistent with fewer cells in S phase as with regulation of the gene itself. Any p53-programme membership selected with the TP53 labels is circular ([[Cross-fitting and circularity]]).

## References

- Tishkoff et al., 1997, PNAS — identified yeast EXO1 as an exonuclease that interacts with MSH2 and acts in mismatch repair.
- Wei et al., 2003, Genes & Development — Exo1-deficient mice show mismatch-repair defects and increased cancer susceptibility.
- Mimitou & Symington, 2008, Nature — Sae2, Exo1 and Sgs1 collaborate in processing DNA double-strand break ends.
- Nimonkar et al., 2011, Genes & Development — reconstituted BLM-DNA2 and EXO1-BLM machineries for human DNA end resection.
- Engeland, 2018, Cell Death and Differentiation — review of indirect transcriptional repression through the p53-p21-DREAM route.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 40 drug-doses (26 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.91× (z +13.8, q 2e-40, up in 39 of 46 measured lines) ⚠ cell-cycle shift, explains ~89% of this change. The strongest without an alert is [[Brivudine (drug)]] 5 µM: 1.98× (z +4.6, q 2e-04, up in 12 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 42 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.645× (z -8.0, q 6e-13, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DTL]] (+0.96, fdr 7e-06), [[CDC45]] (+0.94, fdr 7e-06), [[WDR76]] (+0.94, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 26 with an alert ⚠; shown: the 15 strongest and the 13 next strongest without an alert. 40 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 26 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10487.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **2.91×** | +13.8 | 2e-40 | 39/46 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **2.88×** | +13.6 | 7e-40 | 37/45 (A549, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.78×** | +13.2 | 2e-37 | 42/46 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.84×** | +7.8 | 7e-13 | 31/45 (J82, SW480, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~96% of this change | **1.80×** | +7.3 | 3e-11 | 27/43 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **1.41×** | +6.2 | 5e-08 | 29/46 (SW480, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.57×** | +5.8 | 6e-07 | 23/46 (RKO, SW 900, …) | all doses, stronger at high dose |  |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.36×** | +5.6 | 1e-06 | 26/46 (SW480, LS 180, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~95% of this change | **1.53×** | +5.5 | 3e-06 | 25/45 (PANC-1, C-33 A, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.52×** | +5.4 | 3e-06 | 26/44 (A549, HT-29, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~96% of this change | **1.48×** | +5.0 | 2e-05 | 23/45 (SW480, RKO, …) | all doses, flat |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **1.55×** | +4.8 | 9e-05 | 17/46 (SW480, LS 180, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.7 | 1e-04 | 19/46 (SW480, SW1417, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.98×** | +4.6 | 2e-04 | 12/46 (A549, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +4.4 | 4e-04 | 17/46 (SW480, A-427, …) | top dose only | plate-row cell shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.37×** | +4.1 | 0.001 | 15/46 (A498, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.001 | 19/45 (A-427, LS 180, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.011 | 9/44 (SW480, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.015 | 14/46 (SW480, J82, …) | rises with dose |  |
| [[Methotrexate (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.026 | 7/46 (LS 180, C32, …) | top dose only |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.028 | 11/45 (A-427, LS 180, …) | all doses, flat |  |
| [[Irinotecan (drug)]] 5 µM |  | **1.56×** | +3.0 | 0.042 | 6/46 (SW480, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Berbamine (drug)]] 0.05 µM |  | **1.26×** | +2.9 | 0.054 | 10/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | 1.19× | +2.9 | 0.060 | 8/46 (SW480, C-33 A, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.25×** | +2.8 | 0.069 | 6/46 (NCI-H460, A498, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +2.8 | 0.072 | 10/45 (PANC-1, SW480, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **1.24×** | +2.8 | 0.072 | 9/46 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.50×** | +2.7 | 0.093 | 6/44 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 14 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 42 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10487.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.645×** | -8.0 | 6e-13 | 27/45 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.448×** | -7.0 | 5e-10 | 30/46 (SW480, A498, …) | two highest doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.558×** | -6.3 | 4e-08 | 25/45 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.721×** | -6.0 | 3e-07 | 25/46 (HCT15, RKO, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.580×** | -5.9 | 4e-07 | 24/46 (A498, LS 180, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.742×** | -5.5 | 4e-06 | 22/46 (A498, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.658×** | -5.4 | 5e-06 | 24/45 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.658×** | -5.2 | 1e-05 | 21/45 (NCI-H460, SK-MEL-2, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.757×** | -5.1 | 2e-05 | 21/46 (COLO 205, SHP-77, …) | rises with dose |  |
| [[palbociclib (drug)]] 5 µM |  | **0.472×** | -5.1 | 2e-05 | 22/44 (LoVo, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **0.758×** | -5.1 | 2e-05 | 23/46 (COLO 205, RKO, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.683×** | -4.9 | 4e-05 | 20/46 (A498, NCI-H460, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.691×** | -4.4 | 5e-04 | 19/46 (HCT15, LS 180, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.790×** | -4.3 | 6e-04 | 17/46 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.701×** | -4.2 | 9e-04 | 20/46 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.737×** | -3.9 | 0.002 | 18/45 (NCI-H460, A549, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.744×** | -3.8 | 0.004 | 18/45 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Temsirolimus (drug)]] 5 µM |  | **0.815×** | -3.8 | 0.005 | 15/46 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.653×** | -3.7 | 0.005 | 17/46 (MIA PaCa-2, Hs 766T, …) | two highest doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.709×** | -3.7 | 0.005 | 16/44 (NCI-H661, PANC-1, …) | rises with dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.585×** | -3.6 | 0.007 | 17/43 (LS 180, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | **0.823×** | -3.6 | 0.008 | 20/46 (Panc 03.27, hTERT-HPNE, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **0.827×** | -3.5 | 0.010 | 16/46 (NCI-H460, COLO 205, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.761×** | -3.4 | 0.014 | 19/44 (A-427, HEC-1-A, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.73 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10487. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 54.2 | 0 | 5 (2 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.250× (z -13.1) |
| [[A498 (line)]] | wt | 47.1 | 0 | 5 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.117× (z -18.7) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -12.2) |
| [[SW480 (line)]] | alt | 30.9 | 3 (3 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 3.57× (z +10.4) ⚠ toxic; cell-cycle shift, explains ~96% of this change | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 63.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -11.6) |
| [[A549 (line)]] | wt | 12.8 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.80× (z +10.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 20.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 5.45× (z +8.9) ⚠ cell-cycle shift, explains ~92% of this change | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.1) |
| [[NCI-H2347 (line)]] | alt | 14.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.30× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[C-33 A (line)]] | alt | 62.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[LOX-IMVI (line)]] | wt | 17.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.58× (z +8.8) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 17.5 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.111× (z -14.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[COLO 205 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.114× (z -10.1) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.128× (z -13.9) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 21.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.6) |
| [[J82 (line)]] | alt | 59.9 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 0.5 µM 2.73× (z +9.6) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[LoVo (line)]] | wt | 17.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.132× (z -15.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 7.72 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0752× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 54.3 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.268× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.164× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.310× (z -9.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SHP-77 (line)]] | alt | 87.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.264× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 37.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.259× (z -9.2) |
| [[A-172 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.18 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.93 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.56 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 41.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10487), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTL]] | +0.96 | +0.95 / +0.94 | both halves | 7e-06 | STRING 901 |
| [[CDC45]] | +0.94 | +0.94 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 963 |
| [[WDR76]] | +0.94 | +0.95 / +0.92 | both halves | 7e-06 | STRING 527 |
| [[BLM]] | +0.93 | +0.92 / +0.92 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 998 |
| [[MCM10]] | +0.92 | +0.91 / +0.91 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 954 |
| [[WDHD1]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | STRING 935 |
| [[DSCC1]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | STRING 727 |
| [[RAD54L]] | +0.91 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 832 |
| [[FANCB]] | +0.91 | +0.91 / +0.89 | both halves | 7e-06 | STRING 454 |
| [[CENPK]] | +0.91 | +0.90 / +0.89 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 472 |
| [[ATAD2]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | STRING 510 |
| [[POLQ]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 805 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises EXO1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without E2F2 | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises EXO1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.97× lower at baseline in the lines without E2F8 | 0.019 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[TCF19]] | B | TCF19 activity raises EXO1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.84× lower at baseline in the lines without TCF19 | 0.029 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[MTOR]] | B | MTOR activity raises EXO1's level | compounds that target MTOR: 5 of 8 lower it (AZD-8055, Bimiralisib, Rapamycin, Sapanisertib, Temsirolimus) | 62% of the class's compounds vs 8.1% of all compounds | 0.070 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TOP1]] | B | TOP1 activity lowers EXO1's level | compounds that target TOP1: 3 of 3 raise it (Doxorubicin, Irinotecan, Topotecan) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises EXO1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without FAM111B | 0.097 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises EXO1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.55× lower at baseline in the lines without CDC25A | 0.0995 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[DSCC1]] | C | DSCC1 activity raises EXO1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.97× lower at baseline in the lines without DSCC1 | 0.029 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent; co-absent with the target |
| [[E2F1]], [[MCM3]] | C | E2F1, MCM3 activity raises EXO1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.83× lower at baseline in the lines without E2F1, MCM3 | 0.061 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent genes |
| [[PBK]] | C | PBK activity raises EXO1's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.84× lower at baseline in the lines without PBK | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent; co-absent with the target |
| [[SHMT1]] | C | SHMT1 activity raises EXO1's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.03× lower at baseline in the lines without SHMT1 | 0.065 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent |
| [[MCM10]] | C | MCM10 activity raises EXO1's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 2.83× lower at baseline in the lines without MCM10 | 0.075 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.961). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-34.6, -45.4); signed map (-38.4, -44.3). **Vector** length 150, 50.9% of its response variance represented; |z| ≥ 3 in 1,364 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.71 to 65); *DNA strand elongation* (reactome, mean cos +0.77 to 28); *DNA Replication* (reactome, mean cos +0.77 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +7.1 | +7.8 |
|  | [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~83% of this change | +5.3 | +6.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | +4.6 | +13.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | +13.2 |
|  | [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +4.5 | +5.6 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +3.7 | +4.1 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +3.5 | +4.4 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +3.2 | +3.2 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +3.0 | +2.6 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.9 | +3.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -7.9 | -6.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | -7.2 | -5.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.1 | -8.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | -6.3 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.8 | -6.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.7 | -1.9 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.7 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | exonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:241,847,967-241,895,148 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEX1, hExoI |
| Gene groups (HGNC) | Exonucleases; Rad2/XPG endonuclease family |
| Hallmark sets | G2M_CHECKPOINT |
| Reactome | 36 pathways, smallest: Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha); Mismatch Repair |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ84](https://www.uniprot.org/uniprotkb/Q9UQ84) (Exonuclease 1):

> 5'->3' double-stranded DNA exonuclease which may also possess a cryptic 3'->5' double-stranded DNA exonuclease activity. Functions in DNA mismatch repair (MMR) to excise mismatch-containing DNA tracts directed by strand breaks located either 5' or 3' to the mismatch. Also exhibits endonuclease activity against 5'-overhanging flap structures similar to those generated by displacement synthesis when DNA polymerase encounters the 5'-end of a downstream Okazaki fragment. Required for somatic …

**Summary**, from NCBI Gene [9156](https://www.ncbi.nlm.nih.gov/gene/9156):

> This gene encodes a protein with 5' to 3' exonuclease activity as well as an RNase H activity. It is similar to the Saccharomyces cerevisiae protein Exo1 which interacts with Msh2 and which is involved in mismatch repair and recombination. Alternative splicing of this gene results in three transcript variants encoding two different isoforms. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:3511](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3511) · Entrez [9156](https://www.ncbi.nlm.nih.gov/gene/9156) · UniProt [Q9UQ84](https://www.uniprot.org/uniprotkb/Q9UQ84) · Ensembl [ENSG00000174371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000174371)

## Data

Gene col 10487: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10487); `tables/drug_effects.parquet` (85 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10487, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10487]; `tensor/DDL_lfc|DDL_z.npy` [10487]; `embed/gene_vectors.npy` [10487]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10487 or target_col == 10487). Every well: [[EXO1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/EXO1.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
