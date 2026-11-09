---
symbol: "MCM3"
type: "gene"
col: 3321
ensembl_id: "ENSG00000112118"
name: "minichromosome maintenance complex component 3"
location: "6p12.2"
module: 6
arm: "+"
pooled_cpm: 33.54
n_lines_expressing: 47
n_dd_up: 30
n_dd_down: 18
n_dd_up_clean: 7
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 9
direction_downstream: 58
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM3

*minichromosome maintenance complex component 3* — 6p12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (23 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +15.0, q 0e+00, up in 40 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.39× (z +5.5, q 2e-06, up in 24 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 0.691× (z -6.2, q 3e-07, down in 33 of 45 measured lines) ⚠ cell-cycle shift, explains ~59% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.728× (z -5.3, q 3e-05, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.93, fdr 7e-06), [[WDR76]] (+0.89, fdr 7e-06), [[CDC45]] (+0.88, fdr 7e-06).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[E2F2]] → it (grade B ⚠); 58 go from it, the strongest it → [[MCM4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 23 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 23 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | **3.56×** | +15.0 | 0e+00 | 40/41 (A498, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | **3.12×** | +12.9 | 8e-36 | 36/38 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **2.92×** | +11.7 | 2e-29 | 34/38 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **2.17×** | +8.8 | 2e-16 | 36/44 (C32, LoVo, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.87×** | +7.4 | 2e-11 | 31/45 (LOX-IMVI, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.80×** | +6.9 | 4e-10 | 35/45 (LoVo, Panc 03.27, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.70×** | +6.3 | 3e-08 | 29/43 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.64×** | +5.9 | 3e-07 | 26/44 (LoVo, A549, …) | rises with dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +5.5 | 2e-06 | 24/45 (J82, AN3 CA, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~99% of this change | **1.59×** | +5.5 | 3e-06 | 29/45 (J82, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | **1.62×** | +5.4 | 3e-06 | 28/45 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.57×** | +5.1 | 2e-05 | 24/44 (C32, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.53×** | +5.0 | 3e-05 | 27/44 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **1.52×** | +4.9 | 3e-05 | 26/44 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **2.24×** | +4.8 | 7e-05 | 24/45 (LOX-IMVI, J82, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.79×** | +3.5 | 0.013 | 18/44 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.77×** | +3.4 | 0.015 | 17/44 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.33×** | +3.4 | 0.016 | 14/45 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.040 | 6/45 (Panc 03.27, PANC-1, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.64×** | +2.9 | 0.064 | 16/44 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 1.18× | +2.8 | 0.097 | 11/45 (KATO III, NCI-H23, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.691×** | -6.2 | 3e-07 | 33/45 (RKO, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.728×** | -5.3 | 3e-05 | 27/45 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.693×** | -4.4 | 0.002 | 21/45 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~83% of this change | **0.598×** | -4.4 | 0.002 | 22/45 (PANC-1, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.694×** | -4.3 | 0.002 | 23/44 (SK-MEL-2, NCI-H2030, …) | rises with dose | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.698×** | -4.1 | 0.004 | 21/44 (SW 900, A-172, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.695×** | -4.1 | 0.004 | 23/45 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.768×** | -3.6 | 0.021 | 20/45 (SW480, HEC-1-A, …) | all doses, flat | noisy plate (z scaled) |
| [[RMC-6236 (drug)]] 5 µM |  | **0.573×** | -3.3 | 0.051 | 15/44 (A-427, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.757×** | -3.3 | 0.051 | 16/44 (KATO III, LS 180, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.761×** | -3.3 | 0.051 | 19/45 (A-172, A498, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.825×** | -3.2 | 0.051 | 19/45 (MIA PaCa-2, SHP-77, …) | inconsistent across doses |  |
| [[AZD-8055 (drug)]] 0.5 µM |  | **0.684×** | -3.2 | 0.051 | 13/45 (MIA PaCa-2, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | **0.763×** | -3.2 | 0.051 | 15/44 (KATO III, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.765×** | -3.2 | 0.051 | 14/45 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 0.05 µM |  | **0.765×** | -3.2 | 0.051 | 15/45 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.812×** | -3.1 | 0.056 | 13/45 (SW480, A-427, …) | all doses, flat |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.834× | -3.1 | 0.062 | 16/45 (Hs 766T, HEC-1-A, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +1.24 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 62.8 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -16.5) |
| [[A498 (line)]] | wt | 28.5 | 2 (2 ⚠) | 2 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.87× (z +11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.219× (z -11.3) ⚠ cell-cycle shift, explains ~71% of this change |
| [[J82 (line)]] | alt | 55.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +11.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.10× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[NCI-H460 (line)]] | wt | 16.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.04× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[PANC-1 (line)]] | alt | 34.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.12× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[SNU-1 (line)]] | wt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.111× (z -9.0) |
| [[SNU-423 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.83× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[SW1417 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.72× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[SW480 (line)]] | alt | 71.4 | 1 (1 ⚠) | 1 | [[Digitoxin (drug)]] 0.5 µM 2.68× (z +8.8) ⚠ cell-cycle shift, explains ~88% of this change | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -11.8) |
| [[A-172 (line)]] | wt | 24.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | — |
| [[A549 (line)]] | wt | 11.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[AN3 CA (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 21.1 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.176× (z -8.5) |
| [[Hs 766T (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -9.4) |
| [[KATO III (line)]] | alt | 51.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.57× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | — |
| [[NCI-H23 (line)]] | alt | 73.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -16.9) |
| [[SW48 (line)]] | wt | 52.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.217× (z -8.6) |
| [[AsPC-1 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 84.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 62.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.96 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 36.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.20 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 92.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 49.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 107 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[WDR76]] | +0.89 | +0.88 / +0.87 | both halves | 7e-06 | **novel candidate** |
| [[CDC45]] | +0.88 | +0.88 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 999 |
| [[MCM10]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 999 |
| [[POLA1]] | +0.87 | +0.86 / +0.86 | both halves | 7e-06 | pathway: Activation of the pre-replicative complex; STRING 988 |
| [[MCM5]] | +0.87 | +0.90 / +0.82 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[RANBP1]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[MCM2]] | +0.87 | +0.83 / +0.87 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[HELLS]] | +0.87 | +0.81 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 728 |
| [[CDC25A]] | +0.86 | +0.88 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 553 |
| [[EXO1]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 736 |
| [[CLSPN]] | +0.86 | +0.85 / +0.85 | both halves | 7e-06 | pathway: Activation of ATR in response to replication stress; STRING 952 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 4, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F2]] | B | E2F2 activity raises MCM3's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 2.21× lower at baseline in the lines without E2F2 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises MCM3's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without CDCA7 | 0.088 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[FAM111B]] | B | FAM111B activity raises MCM3's level | lines that do not express FAM111B (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without FAM111B | 0.089 | ⚠ within organs, on part of the lines; also absent: E2F8, SLC37A2; maybe low, not absent |
| [[POGLUT3]] | B | POGLUT3 activity raises MCM3's level | lines that do not express POGLUT3 (5) vs lines expressing it (45) | 1.83× lower at baseline in the lines without POGLUT3 | 0.097 | ⚠ within organs, on part of the lines; also absent: DENND2B, MEX3A, CAMKK1 |
| [[CDC25A]] | C | CDC25A activity raises MCM3's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 3.36× lower at baseline in the lines without CDC25A | 0.019 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent; co-absent with the target |
| [[MCM10]] | C | MCM10 activity raises MCM3's level | lines that do not express MCM10 (4) vs lines expressing it (46) | 3.31× lower at baseline in the lines without MCM10 | 0.038 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: E2F1, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target |
| [[TCF19]] | C | TCF19 activity raises MCM3's level | lines that do not express TCF19 (5) vs lines expressing it (45) | 2.63× lower at baseline in the lines without TCF19 | 0.047 | ⚠ within organs, on part of the lines; also absent: CLSPN, AURKB, SMARCD3; maybe low, not absent; co-absent with the target |
| [[SHMT1]] | C | SHMT1 activity raises MCM3's level | lines that do not express SHMT1 (3) vs lines expressing it (47) | 3.69× lower at baseline in the lines without SHMT1 | 0.072 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: TLCD3B, CDC25A, DBNDD1; maybe low, not absent; co-absent with the target |
| [[CDC45]], [[CENPM]], [[SKA3]] | C | CDC45, CENPM, SKA3 activity raises MCM3's level | lines that do not express CDC45, CENPM, SKA3 (3) vs lines expressing them (47) | 2.88× lower at baseline in the lines without CDC45, CENPM, SKA3 | 0.098 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: CLSPN, SLC44A2, AURKB; maybe low, not absent; co-absent with the target; co-absent genes |

### Downstream of this gene

*58 arrows, 58 of them with an alert ⚠; grade A 0, B 0, C 58. Shown: the 12 strongest; 46 more arrows (46 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCM4]] | C | [[E2F1]], MCM3 activity raises MCM4's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.73× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[PCNA]] | C | [[E2F1]], MCM3 activity raises PCNA's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.46× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[SKA3]] | C | [[E2F1]], MCM3 activity raises SKA3's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.31× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CLSPN]] | C | [[E2F1]], MCM3 activity raises CLSPN's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.30× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[SHMT1]] | C | MCM3 activity raises SHMT1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 3.18× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p |
| [[LMNB1]] | C | MCM3 activity raises LMNB1's level | lines that do not express MCM3 (3) vs lines expressing it (47) | 3.14× lower at baseline in the lines without MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p |
| [[GINS1]] | C | [[E2F1]], MCM3 activity raises GINS1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 3.11× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[POLQ]] | C | [[E2F1]], MCM3 activity raises POLQ's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.91× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[TK1]] | C | [[E2F1]], MCM3 activity raises TK1's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.88× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[CEP78]] | C | [[E2F1]], MCM3 activity raises CEP78's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.86× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |
| [[PCLAF]] | C | [[E2F1]], MCM3 activity raises PCLAF's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.82× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; co-absent with the target; its own permutation p; co-absent genes |
| [[GMNN]] | C | [[E2F1]], MCM3 activity raises GMNN's level | lines that do not express E2F1, MCM3 (3) vs lines expressing them (47) | 2.76× lower at baseline in the lines without E2F1, MCM3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MCM10, AURKB, ENSG00000197332; maybe low, not absent; its own permutation p; co-absent genes |

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.913). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.6, -43.5); signed map (-36.9, -46.2). **Vector** length 135, 46.7% of its response variance represented; |z| ≥ 3 in 1,197 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.71 to 32); *Chromosome Maintenance* (reactome, mean cos +0.70 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.71 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | +5.4 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | +5.0 | +11.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~75% of this change | +4.7 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~73% of this change | +4.5 | +15.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.4 | +5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.9 | +2.0 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +1.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.5 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.7 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -4.4 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.1 | -6.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -4.7 | -2.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.1 | -2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.0 | -2.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -3.4 | -2.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -2.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p12.2 — chr6:52,264,014-52,284,881 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MCM family; minichromosome maintenance 2-7 complex |
| Hallmark sets | G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 17 pathways, smallest: Unwinding of DNA; Activation of the pre-replicative complex; DNA strand elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P25205](https://www.uniprot.org/uniprotkb/P25205) (DNA replication licensing factor MCM3):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4172](https://www.ncbi.nlm.nih.gov/gene/4172):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are involved in the initiation of eukaryotic genome replication. The hexameric protein complex formed by MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. This protein is a subunit of the protein complex that consists of MCM2-7. It has been …

**Accessions** — [HGNC:6945](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6945) · Entrez [4172](https://www.ncbi.nlm.nih.gov/gene/4172) · UniProt [P25205](https://www.uniprot.org/uniprotkb/P25205) · Ensembl [ENSG00000112118](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112118)

## Data

Gene col 3321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3321); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3321]; `tensor/DDL_lfc|DDL_z.npy` [3321]; `embed/gene_vectors.npy` [3321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3321 or target_col == 3321). Every well: [[MCM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
