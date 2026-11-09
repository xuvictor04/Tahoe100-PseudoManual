---
symbol: "NOTCH2NLB"
type: "gene"
col: 16182
ensembl_id: "ENSG00000286019"
name: "notch 2 N-terminal like B"
location: "1q21.2"
module: 226
arm: "+"
pooled_cpm: 7.34
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/226"]
generated_by: "tahoemap"
---

# NOTCH2NLB

*notch 2 N-terminal like B* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.64× (z +23.1, q 0e+00, up in 38 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (8 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.471× (z -7.7, q 1e-11, down in 22 of 29 measured lines) ⚠ toxic. The strongest without an alert is [[Berbamine (drug)]] 0.5 µM: 0.642× (z -4.7, q 2e-04, down in 19 of 42 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.0776×, NCI-H1792 0.0763×; ⚠ transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.0887×, HS-578T 0.0912×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.119×, CFPAC-1 0.111×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.188×, PANC-1 0.158×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0950×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NOTCH2NLC]] (+0.77, fdr 7e-06), [[NBPF10]] (+0.76, fdr 7e-06), [[NOTCH2NLA]] (+0.72, fdr 7e-06); moves opposite to [[PPT2]] (-0.71, fdr 7e-06), [[SLC9A6]] (-0.66, fdr 1e-05), [[NFATC3]] (-0.64, fdr 1e-05).
> It is in [[Module 226]], a single-armed module (NOTCH2 Activation and Transmission of Signal to the Nucleus).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ITGA1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 16182.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.64×** | +23.1 | 0e+00 | 38/38 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **3.47×** | +12.7 | 1e-34 | 41/43 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.29×** | +8.8 | 2e-16 | 25/40 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.87×** | +6.7 | 4e-09 | 27/45 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.53×** | +4.6 | 5e-04 | 20/44 (A498, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +4.4 | 0.001 | 16/43 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.40×** | +3.6 | 0.022 | 12/43 (NCI-H2030, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.38×** | +3.4 | 0.040 | 12/43 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.44×** | +3.4 | 0.050 | 6/39 (BT-474, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.067 | 10/42 (A498, HEC-1-A, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.33× | +3.0 | 0.12 | 11/38 (NCI-H460, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.32× | +3.0 | 0.12 | 9/43 (PANC-1, NCI-H1792, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 10 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 16182.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Pimozide (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.0776×, NCI-H1792 0.0763×; ⚠ transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1792 0.0887×, HS-578T 0.0912×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM in 2 lines (SK-MEL-2 0.119×, CFPAC-1 0.111×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.188×, PANC-1 0.158×); [[Allantoin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0950×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.471×** | -7.7 | 1e-11 | 22/29 (Panc 03.27, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.579×** | -5.8 | 2e-06 | 21/27 (HS-578T, A498, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.594×** | -5.3 | 2e-05 | 10/12 (NCI-H1792, HS-578T, …) | rises with dose | composition shift; position effect removed |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.592×** | -5.3 | 2e-05 | 20/44 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.605×** | -5.0 | 5e-05 | 21/45 (NCI-H2030, A-427, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.867× | -4.9 | 1e-04 | 21/46 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.5 µM |  | **0.642×** | -4.7 | 2e-04 | 19/42 (LoVo, HOP62, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.688×** | -3.9 | 0.006 | 11/44 (C32, J82, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.724×** | -3.4 | 0.044 | 11/45 (HOP62, J82, …) | two highest doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.802×** | -3.3 | 0.064 | 6/45 (H4, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 0.750× | -3.0 | 0.12 | 13/38 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Ranolazine (drug)]] 0.5 µM |  | 0.750× | -3.0 | 0.12 | 14/43 (MIA PaCa-2, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.38 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 16182. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 18.2 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.00× (z +16.1) | [[Ivabradine (hydrochloride) (drug)]] 0.5 µM 0.198× (z -9.3) ⚠ transcription drop; unreliable plate only |
| [[PANC-1 (line)]] | alt | 5.13 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 17.6× (z +20.7) | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.158× (z -9.5) |
| [[A498 (line)]] | wt | 6.53 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.151× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H1792 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Pimozide (drug)]] 0.5 µM 0.0763× (z -13.2) ⚠ transcription drop · without an alert: [[Glycyrrhizic acid (drug)]] 0.05 µM 0.0950× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 15.6 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +13.0) | [[Pimozide (drug)]] 0.5 µM 0.0776× (z -15.0) ⚠ transcription drop · without an alert: [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.188× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 4.92 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +11.6) | [[Allantoin (drug)]] 0.5 µM 0.0950× (z -11.6) |
| [[Panc 03.27 (line)]] | alt | 17.6 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.52× (z +11.6) | [[Simotinib (drug)]] 5 µM 0.0844× (z -12.8) ⚠ toxic |
| [[A549 (line)]] | wt | 5.91 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.34× (z +11.4) | [[Brimonidine (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[HS-578T (line)]] | alt | 9.45 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 10.4 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.76× (z +11.3) | [[Pimozide (drug)]] 0.05 µM 0.155× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 6.39 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.33× (z +9.8) | [[Docetaxel (drug)]] 0.05 µM 0.0952× (z -9.9) ⚠ transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.14 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.60× (z +8.9) | [[Nimesulide (drug)]] 5 µM 0.0959× (z -9.6) ⚠ toxic; unreliable plate only |
| [[AsPC-1 (line)]] | alt | 6.41 | 0 | 1 | — | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.0655× (z -9.6) |
| [[C32 (line)]] | wt | 7.18 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0775× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 8.05 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.111× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 4.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.57× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.55× (z +10.3) | — |
| [[LoVo (line)]] | wt | 4.34 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.97× (z +9.5) | — |
| [[LOX-IMVI (line)]] | wt | 7.75 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0886× (z -9.8) ⚠ toxic |
| [[RPMI-7951 (line)]] | alt | 7.48 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.119× (z -10.3) |
| [[SNU-423 (line)]] | alt | 16.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0781× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.12 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.70 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.86 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 16182), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*40 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLC]] | +0.77 | +0.70 / +0.74 | both halves | 7e-06 | pathway: Expression of NOTCH2NL genes |
| [[NBPF10]] | +0.76 | +0.75 / +0.73 | both halves | 7e-06 | STRING 543 |
| [[NOTCH2NLA]] | +0.72 | +0.62 / +0.77 | both halves | 7e-06 | pathway: Expression of NOTCH2NL genes; STRING 410 |
| [[NBPF26]] | +0.67 | +0.57 / +0.69 | both halves | 1e-05 |  |
| [[APLF]] | +0.65 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[NBPF19]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 | STRING 515 |
| [[NBPF14]] | +0.61 | +0.59 / +0.64 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[CGGBP1]] | +0.60 | +0.65 / +0.43 | both halves | 3e-05 |  |
| [[NEPRO-AS1]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[LACC1]] | +0.59 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[DZIP3]] | +0.58 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EEA1]] | +0.57 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[HIVEP2]] | +0.57 | +0.41 / +0.54 | both halves | 4e-05 |  |

## Genes that move opposite

*60 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPT2]] | -0.71 | -0.63 / -0.61 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.66 | -0.66 / -0.56 | both halves | 1e-05 |  |
| [[NFATC3]] | -0.64 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.62 | -0.63 / -0.60 | both halves | 7e-06 |  |
| [[ADPGK]] | -0.62 | -0.70 / -0.49 | both halves | 1e-05 |  |
| [[USPL1]] | -0.61 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[TYW1]] | -0.60 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[LSM12]] | -0.60 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[STRAP]] | -0.60 | -0.62 / -0.40 | both halves | 5e-05 |  |
| [[GRB2]] | -0.59 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[INPP5B]] | -0.59 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[SNHG30]] | -0.59 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA1]] | B | ITGA1 activity raises NOTCH2NLB's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 1.55× lower at baseline in the lines without ITGA1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973 |
| [[HMGN2P46]] | B | HMGN2P46 activity raises NOTCH2NLB's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without HMGN2P46 | 0.042 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 226]] — NOTCH2 Activation and Transmission of Signal to the Nucleus; 9 genes; every member is in the + arm (projection on the module's main direction 0.854). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.53; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (0.5, -29.3); signed map (44.4, -15.6). **Vector** length 65.9, 9.97% of its response variance represented; |z| ≥ 3 in 1,213 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.1 | +23.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.1 | +12.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.4 | +8.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +4.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | +4.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.2 | +1.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +3.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +1.1 | +2.5 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.5 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -2.4 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -2.3 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.1 | -2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.5 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | notch 2 N-terminal like B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:148,600,285-148,679,746 (-) |
| Ensembl biotype | protein_coding |
| Reactome | 6 pathways, smallest: Expression of NOTCH2NL genes; NOTCH2 Activation and Transmission of Signal to the Nucleus; Signaling by NOTCH2 |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DPK3](https://www.uniprot.org/uniprotkb/P0DPK3) (Notch homolog 2 N-terminal-like protein B):

> Human-specific protein that promotes neural progenitor proliferation and evolutionary expansion of the brain neocortex by regulating the Notch signaling pathway. Able to promote neural progenitor self-renewal, possibly by down-regulating neuronal differentiation genes, thereby delaying the differentiation of neuronal progenitors and leading to an overall final increase in neuronal production. Acts by enhancing the Notch signaling pathway via two different mechanisms that probably work in …

**Summary**, from NCBI Gene [100996763](https://www.ncbi.nlm.nih.gov/gene/100996763):

> Enables Notch binding activity. Involved in cerebral cortex development and positive regulation of Notch signaling pathway. Located in extracellular region; nucleoplasm; and plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:53923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:53923) · Entrez [100996763](https://www.ncbi.nlm.nih.gov/gene/100996763) · UniProt [P0DPK3](https://www.uniprot.org/uniprotkb/P0DPK3) · Ensembl [ENSG00000286019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000286019)

## Data

Gene col 16182: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 16182); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 16182, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 16182]; `tensor/DDL_lfc|DDL_z.npy` [16182]; `embed/gene_vectors.npy` [16182]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 16182 or target_col == 16182). Every well: [[NOTCH2NLB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOTCH2NLB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
