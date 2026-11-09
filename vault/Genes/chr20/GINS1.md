---
symbol: "GINS1"
type: "gene"
col: 2058
ensembl_id: "ENSG00000101003"
name: "GINS complex subunit 1"
location: "20p11.21"
module: 6
arm: "+"
pooled_cpm: 21.77
n_lines_expressing: 49
n_dd_up: 41
n_dd_down: 18
n_dd_up_clean: 12
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 20
direction_downstream: 1
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# GINS1

*GINS complex subunit 1* — 20p11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 41 drug-doses (29 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.74× (z +11.8, q 1e-29, up in 31 of 46 measured lines) ⚠ cell-cycle shift, explains ~50% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.20× (z +4.0, q 0.002, up in 11 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (7 with an alert ⚠); the strongest is [[palbociclib (drug)]] 0.5 µM: 0.577× (z -5.9, q 2e-06, down in 24 of 47 measured lines) ⚠ cell-cycle shift, explains ~63% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.705× (z -5.3, q 2e-05, down in 24 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDHD1]] (+0.92, fdr 7e-06), [[MELK]] (+0.91, fdr 7e-06), [[POLQ]] (+0.90, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[TCF19]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DYNC2I2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 31 with an alert ⚠; shown: the 15 strongest and the 12 next strongest without an alert. 41 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 29 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2058.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.74×** | +11.8 | 1e-29 | 31/46 (A549, SNU-423, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **2.08×** | +11.1 | 5e-26 | 39/46 (A549, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **2.05×** | +10.8 | 4e-25 | 37/47 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.94×** | +10.0 | 1e-21 | 36/47 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.85×** | +9.3 | 1e-18 | 29/40 (NCI-H1573, A549, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~66% of this change | **1.76×** | +8.2 | 2e-14 | 24/43 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.69×** | +7.7 | 1e-12 | 21/27 (A549, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.62×** | +7.0 | 1e-10 | 30/46 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +6.4 | 1e-08 | 28/47 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.50×** | +6.2 | 4e-08 | 25/46 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.51×** | +5.9 | 1e-07 | 18/47 (LoVo, SNU-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **1.47×** | +5.4 | 3e-06 | 17/34 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **1.27×** | +5.2 | 9e-06 | 26/47 (NCI-H2347, LoVo, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **1.24×** | +4.6 | 2e-04 | 17/47 (NCI-H23, HT-29, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.35×** | +4.5 | 2e-04 | 16/46 (LoVo, H4, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.20×** | +4.0 | 0.002 | 11/47 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **1.27×** | +3.3 | 0.017 | 8/46 (LoVo, NCI-H460, …) | all doses, flat |  |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.028 | 12/46 (HT-29, A-427, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.2 | 0.028 | 10/44 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.030 | 10/46 (A-427, NCI-H1573, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.032 | 10/44 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.48×** | +3.1 | 0.032 | 8/47 (A549, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.035 | 12/47 (A549, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 0.05 µM |  | **1.24×** | +3.0 | 0.037 | 5/46 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Lopinavir (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.050 | 4/46 (NCI-H23, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Lopinavir (drug)]] 0.05 µM |  | **1.21×** | +2.8 | 0.063 | 3/46 (SW480, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.42×** | +2.8 | 0.070 | 7/44 (MIA PaCa-2, A549, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2058.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.577×** | -5.9 | 2e-06 | 24/47 (SW480, KATO III, …) | two highest doses | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.673×** | -5.6 | 5e-06 | 22/46 (H4, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.705×** | -5.3 | 2e-05 | 24/46 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.727×** | -4.8 | 2e-04 | 21/46 (A498, H4, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **0.813×** | -4.4 | 0.001 | 19/47 (HCT15, KATO III, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.761×** | -4.1 | 0.004 | 18/46 (CHP-212, RKO, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~69% of this change | **0.758×** | -3.9 | 0.007 | 16/47 (Hs 766T, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.800×** | -3.8 | 0.012 | 19/47 (HEC-1-A, HOP62, …) | two highest doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.784×** | -3.7 | 0.015 | 16/47 (A-172, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.5 µM |  | **0.785×** | -3.7 | 0.015 | 19/44 (NCI-H460, NCI-H1792, …) | inconsistent across doses | position effect removed |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.719×** | -3.6 | 0.019 | 13/47 (PANC-1, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[palbociclib (drug)]] 5 µM |  | **0.648×** | -3.4 | 0.030 | 16/45 (KATO III, PANC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Berbamine (drug)]] 5 µM |  | 0.853× | -3.4 | 0.032 | 9/47 (RKO, J82, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~82% of this change | **0.803×** | -3.3 | 0.038 | 14/47 (MIA PaCa-2, H4, …) | all doses, flat |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.806×** | -3.3 | 0.042 | 12/46 (H4, NCI-H23, …) | all doses, flat | low cells (technical?) |
| [[Cepharanthine (drug)]] 5 µM |  | 0.863× | -3.1 | 0.058 | 16/47 (RPMI-7951, LoVo, …) | top dose only |  |
| [[Tadalafil (drug)]] 5 µM |  | **0.806×** | -3.1 | 0.058 | 16/46 (Panc 03.27, SNU-423, …) | top dose only |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **0.815×** | -3.1 | 0.065 | 8/46 (H4, A549, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | **0.678×** | -3.1 | 0.065 | 12/43 (LoVo, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | 0.867× | -3.0 | 0.066 | 12/47 (H4, Hs 766T, …) | top dose only |  |
| [[Rapamycin (drug)]] 5 µM |  | 0.871× | -2.9 | 0.083 | 13/47 (NCI-H661, RKO, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.17 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2058. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.6 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.84× (z +11.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-427 (line)]] | wt | 30.5 | 0 | 3 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0957× (z -17.8) ⚠ cell-cycle shift, explains ~50% of this change |
| [[A498 (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.350× (z -9.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW48 (line)]] | wt | 22.8 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.0547× (z -12.4) |
| [[HEC-1-A (line)]] | alt | 55.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 25.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 27.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 20.0 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +8.6) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[RKO (line)]] | wt | 34.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.65× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.64× (z +9.1) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A-172 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.13 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2058), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDHD1]] | +0.92 | +0.89 / +0.94 | both halves | 7e-06 | STRING 996 |
| [[MELK]] | +0.91 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 606 |
| [[POLQ]] | +0.90 | +0.89 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[MCM10]] | +0.90 | +0.87 / +0.89 | both halves | 7e-06 | pathway: DNA Replication; STRING 965 |
| [[DTL]] | +0.90 | +0.88 / +0.90 | both halves | 7e-06 | STRING 513 |
| [[CENPK]] | +0.89 | +0.89 / +0.89 | both halves | 7e-06 | STRING 479 |
| [[EXO1]] | +0.89 | +0.87 / +0.91 | both halves | 7e-06 | STRING 539 |
| [[ATAD5]] | +0.89 | +0.85 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[FANCI]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[CDC45]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | pathway: DNA Replication; STRING 999 |
| [[WDR76]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 |  |
| [[CHAF1A]] | +0.87 | +0.87 / +0.86 | both halves | 7e-06 | STRING 515 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 10, C 10. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF19]] | B | TCF19 activity raises GINS1's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.85× lower at baseline in the lines without TCF19 | 0.009 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent |
| [[CDC25A]] | B | CDC25A activity raises GINS1's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 2.89× lower at baseline in the lines without CDC25A | 0.012 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F8]] | B | E2F8 activity raises GINS1's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 2.79× lower at baseline in the lines without E2F8 | 0.013 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises GINS1's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.23× lower at baseline in the lines without E2F2 | 0.028 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[TLCD3B]] | B | TLCD3B activity raises GINS1's level | lines that do not express TLCD3B (5) vs lines expressing it (45) | 2.47× lower at baseline in the lines without TLCD3B | 0.033 | ⚠ within organs, on part of the lines; also absent: NECAB2, SHMT1, TMCC1-DT; maybe low, not absent |
| [[ZNF724]] | B | ZNF724 activity weakens GINS1's drug response | lines that do not express ZNF724 (7) vs lines expressing it (40) | the lines without ZNF724 respond 1.42× as strongly (z diff -0.87); strongest at Panobinostat 5 µM: 2.88x vs 2.03x (z diff -2.2) | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000283201, ENSG00000269237, ZNF577; target measured in part of the lines; artifact flags |
| [[FAM111B]] | B | FAM111B activity raises GINS1's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.79× lower at baseline in the lines without FAM111B | 0.038 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers GINS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDCA7]] | B | CDCA7 activity raises GINS1's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.13× lower at baseline in the lines without CDCA7 | 0.070 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[ZNF66]] | B | ZNF66 activity raises GINS1's level | lines that do not express ZNF66 (12) vs lines expressing it (38) | 1.23× lower at baseline in the lines without ZNF66 | 0.089 | ⚠ within organs, on part of the lines; also absent: ZNF737, ZNF100, ZNF85 |
| [[DSCC1]] | C | DSCC1 activity raises GINS1's level | lines that do not express DSCC1 (4) vs lines expressing it (46) | 2.96× lower at baseline in the lines without DSCC1 | 0.014 | ⚠ few lines (4 vs 46); across organs; also absent: NDC80, ADGRL1, MYBL2; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises GINS1's level | lines that do not express AURKB (4) vs lines expressing it (46) | 3.12× lower at baseline in the lines without AURKB | 0.020 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNC2I2]] | C | GINS1's natural level strengthens DYNC2I2's drug response | GINS1's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse -0.41; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.927). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.6, -46.1); signed map (-39.4, -44.8). **Vector** length 123, 35.0% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F G1/S* (control, mean cos +0.72 to 23); *Cell Cycle Checkpoints* (reactome, mean cos +0.76 to 45); *Activation of the pre-replicative complex* (reactome, mean cos +0.77 to 22).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | +5.2 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +4.2 | +7.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~58% of this change | +3.9 | +4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +3.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +3.7 | +9.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.4 | +3.3 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | +2.3 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.3 | +2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | +2.3 | +2.1 |
|  | [[Raltitrexed (drug)]] 0.5 µM |  | +2.2 | +3.2 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~81% of this change | -4.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -2.7 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.3 | -2.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.3 | -5.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~35% of this change | -3.7 | -5.6 |
|  | [[palbociclib (drug)]] 5 µM |  | -3.0 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.0 | -3.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.0 | -2.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | GINS complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p11.21 — chr20:25,391,008-25,452,700 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0186, PSF1 |
| Gene groups (HGNC) | GINS complex |
| Hallmark sets | E2F_TARGETS |
| Reactome | 7 pathways, smallest: Unwinding of DNA; DNA strand elongation; Synthesis of DNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14691](https://www.uniprot.org/uniprotkb/Q14691) (DNA replication complex GINS protein PSF1):

> Required for correct functioning of the GINS complex, a complex that plays an essential role in the initiation of DNA replication, and progression of DNA replication forks. GINS complex is a core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built.

**Summary**, from NCBI Gene [9837](https://www.ncbi.nlm.nih.gov/gene/9837):

> The yeast heterotetrameric GINS complex is made up of Sld5 (GINS4; MIM 610611), Psf1, Psf2 (GINS2; MIM 610609), and Psf3 (GINS3; MIM 610610). The formation of the GINS complex is essential for the initiation of DNA replication in yeast and Xenopus egg extracts (Ueno et al., 2005 [PubMed 16287864]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28980](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28980) · Entrez [9837](https://www.ncbi.nlm.nih.gov/gene/9837) · UniProt [Q14691](https://www.uniprot.org/uniprotkb/Q14691) · Ensembl [ENSG00000101003](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101003)

## Data

Gene col 2058: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2058); `tables/drug_effects.parquet` (65 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2058, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2058]; `tensor/DDL_lfc|DDL_z.npy` [2058]; `embed/gene_vectors.npy` [2058]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2058 or target_col == 2058). Every well: [[GINS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GINS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
