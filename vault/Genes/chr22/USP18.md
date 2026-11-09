---
symbol: "USP18"
type: "gene"
col: 11598
ensembl_id: "ENSG00000184979"
name: "ubiquitin specific peptidase 18"
location: "22q11.21"
module: 32
arm: "+"
pooled_cpm: 21.63
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 59
n_dd_up_clean: 11
n_dd_down_clean: 51
in_vector_space: true
direction_upstream: 70
direction_downstream: 43
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# USP18

*ubiquitin specific peptidase 18* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.71× (z +5.2, q 1e-04, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 59 drug-doses (8 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.339× (z -14.8, q 0e+00, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.96, fdr 7e-06), [[PARP9]] (+0.93, fdr 7e-06), [[OAS3]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 70 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 43 go from it, the strongest it → [[IFIT5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11598.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.71×** | +5.2 | 1e-04 | 29/43 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.71×** | +4.9 | 3e-04 | 25/44 (Panc 03.27, LoVo, …) | inconsistent across doses | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.56×** | +4.4 | 0.003 | 22/43 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.38×** | +3.7 | 0.024 | 17/44 (AsPC-1, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.024 | 22/44 (CFPAC-1, C-33 A, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.032 | 16/43 (AsPC-1, NCI-H23, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.29×** | +3.5 | 0.038 | 17/44 (AsPC-1, HS-578T, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.057 | 18/44 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.080 | 12/43 (A549, A498, …) | top dose only |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.080 | 13/44 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.080 | 19/43 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 1.37× | +3.1 | 0.11 | 14/43 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | 1.36× | +3.0 | 0.11 | 11/43 (C32, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 59 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 59 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11598.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.339×** | -14.8 | 0e+00 | 32/44 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.402×** | -12.4 | 5e-33 | 32/44 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.308×** | -11.4 | 1e-27 | 33/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.310×** | -11.3 | 2e-27 | 32/43 (A498, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.298×** | -11.0 | 3e-26 | 35/43 (A498, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.325×** | -10.8 | 2e-25 | 32/43 (A-172, LoVo, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.358×** | -9.9 | 3e-21 | 31/43 (MIA PaCa-2, RKO, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.359×** | -9.9 | 3e-21 | 26/43 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.360×** | -9.9 | 4e-21 | 33/43 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.363×** | -9.8 | 8e-21 | 31/43 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.379×** | -9.4 | 4e-19 | 33/44 (LoVo, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.378×** | -9.0 | 8e-18 | 29/40 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.394×** | -9.0 | 1e-17 | 31/44 (RKO, NCI-H1792, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.400×** | -8.8 | 4e-17 | 33/43 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.412×** | -8.5 | 5e-16 | 32/43 (A549, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.568×** | -7.7 | 5e-13 | 29/44 (SNU-423, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.249×** | -7.0 | 8e-11 | 28/40 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11598. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 28.7 | 0 | 20 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -18.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.177× (z -13.7) |
| [[LoVo (line)]] | wt | 50.8 | 0 | 19 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0690× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (drug)]] 5 µM 0.170× (z -15.2) |
| [[A498 (line)]] | wt | 31.1 | 0 | 12 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.141× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 41.1 | 0 | 11 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0858× (z -17.2) |
| [[NCI-H2347 (line)]] | alt | 59.4 | 0 | 11 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.288× (z -13.6) |
| [[RKO (line)]] | wt | 31.8 | 0 | 11 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0242× (z -15.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM 0.0497× (z -13.0) |
| [[SNU-423 (line)]] | alt | 22.2 | 0 | 11 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.0854× (z -16.1) |
| [[A-172 (line)]] | wt | 28.7 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0460× (z -17.1) |
| [[COLO 205 (line)]] | alt | 61.8 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.143× (z -12.1) |
| [[NCI-H1792 (line)]] | alt | 26.6 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0876× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 23.6 | 0 | 8 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0922× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.108× (z -11.4) |
| [[HS-578T (line)]] | alt | 23.7 | 0 | 7 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0420× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.153× (z -10.2) |
| [[RPMI-7951 (line)]] | alt | 30.4 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.145× (z -13.0) |
| [[C-33 A (line)]] | alt | 35.6 | 0 | 6 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0864× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 19.2 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0474× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.167× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 43.9 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.258× (z -12.6) |
| [[NCI-H1573 (line)]] | alt | 23.2 | 1 (1 ⚠) | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +8.7) ⚠ cell-cycle shift, explains ~85% of this change | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.191× (z -9.9) |
| [[BT-474 (line)]] | alt | 30.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.139× (z -13.4) |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.135× (z -10.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.172× (z -9.5) |
| [[KATO III (line)]] | alt | 19.2 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.233× (z -9.4) |
| [[NCI-H460 (line)]] | wt | 7.89 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +13.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[Panc 03.27 (line)]] | alt | 58.3 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.309× (z -10.1) |
| [[SK-MEL-2 (line)]] | alt | 42.6 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.109× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.314× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 12.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +8.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[LS 180 (line)]] | wt | 12.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SNU-1 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0863× (z -8.8) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.45 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.32 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.57 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.30 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11598), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 883 |
| [[PARP9]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 698 |
| [[OAS3]] | +0.92 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 910 |
| [[IFIT1]] | +0.92 | +0.90 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 949 |
| [[OAS2]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 916 |
| [[MX1]] | +0.92 | +0.88 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 958 |
| [[OAS1]] | +0.90 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 960 |
| [[RIGI]] | +0.90 | +0.90 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 940 |
| [[HERC6]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 902 |
| [[IFI44]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 939 |
| [[IFIT3]] | +0.89 | +0.85 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 902 |
| [[MX2]] | +0.88 | +0.79 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 931 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*70 arrows, 70 of them with an alert ⚠; grade A 0, B 39, C 31. Shown: the 12 strongest; 58 more arrows (58 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises USP18's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS1]] | B | OAS1 activity raises USP18's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity raises USP18's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without IFI6 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[IFI27]] | B | IFI27 activity raises USP18's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.42× lower at baseline in the lines without IFI27 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[CMPK2]] | B | CMPK2 activity raises USP18's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.90× lower at baseline in the lines without CMPK2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[MX1]] | B | MX1 activity raises USP18's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.46× lower at baseline in the lines without MX1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[TRIM22]] | B | TRIM22 activity raises USP18's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.36× lower at baseline in the lines without TRIM22 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[RASGRP3]] | B | RASGRP3 activity raises USP18's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.36× lower at baseline in the lines without RASGRP3 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises USP18's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.98× lower at baseline in the lines without SAMD9L | 0.006 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[RSAD2]] | B | RSAD2 activity raises USP18's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.16× lower at baseline in the lines without RSAD2 | 0.007 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CCDC194]] | B | CCDC194 activity raises USP18's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.09× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[FBXO39]] | B | FBXO39 activity raises USP18's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without FBXO39 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |

### Downstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 0, C 43. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFIT5]] | C | USP18's natural level strengthens IFIT5's drug response | USP18's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.76; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | USP18's natural level strengthens PARP10's drug response | USP18's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.63; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | USP18's natural level strengthens IRF9's drug response | USP18's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.75; direction not clear | 0.009 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | USP18's natural level strengthens SAMHD1's drug response | USP18's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.72; direction not clear | 0.010 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | USP18's natural level strengthens CMTR1's drug response | USP18's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.011 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | USP18 activity raises ADAR's level | lines that do not express USP18 (4) vs lines expressing it (46) | 2.10× lower at baseline in the lines without USP18 | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000280007, OAS3; maybe low, not absent |
| [[ADAR]] | C | USP18 activity strengthens ADAR's drug response | lines that do not express USP18 (4) vs lines expressing it (45) | the lines without USP18 respond 0.29× as strongly (z diff +3.87); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.92x vs 0.63x (z diff +5.8) | 0.012 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000280007, OAS3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PARP12]] | C | USP18's natural level strengthens PARP12's drug response | USP18's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.73; direction not clear | 0.017 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[OAS3]] | C | USP18 activity raises OAS3's level | lines that do not express USP18 (4) vs lines expressing it (46) | 4.61× lower at baseline in the lines without USP18 | 0.023 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ENSG00000280007, OAS3; maybe low, not absent; co-absent with the target |
| [[ISG15]] | C | USP18's natural level strengthens ISG15's drug response | USP18's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.38; direction not clear | 0.025 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[CMPK2]] | C | USP18's natural level strengthens CMPK2's drug response | USP18's natural level across 37 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.80; direction not clear | 0.027 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | USP18's natural level strengthens IFIT1's drug response | USP18's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.48; direction not clear | 0.031 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.934). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.9, 53.9); signed map (65.1, 31.8). **Vector** length 148, 52.8% of its response variance represented; |z| ≥ 3 in 1,450 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.87 to 23); *Interferon gamma signaling* (reactome, mean cos +0.78 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.83 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.4 | +2.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +6.1 | -1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.9 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +1.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.2 | +3.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.8 | +3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | -0.2 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.3 | +4.9 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.4 | -14.8 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -9.0 | -12.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.7 | -10.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.5 | -9.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.2 | -9.9 |

## What is on record

|  |  |
|---|---|
| Name | ubiquitin specific peptidase 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:18,149,843-18,177,397 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Ubiquitin specific peptidases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 30 pathways, smallest: Regulation of IFNA/IFNB signaling; Regulation of NF-kappa B signaling; TAK1-dependent IKK and NF-kappa-B activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UMW8](https://www.uniprot.org/uniprotkb/Q9UMW8) (Ubl carboxyl-terminal hydrolase 18):

> Interferon-induced ISG15-specific protease that plays a crucial role for maintaining a proper balance of ISG15-conjugated proteins in cells. Regulates protein ISGylation by efficiently cleaving ISG15 conjugates linked via isopeptide bonds. Acts as a negative regulator of cGAS-STING signaling be mediating deISGylation of CGAS. Regulates T-cell activation and T-helper 17 (Th17) cell differentiation by deubiquitinating TAK1, likely to keep TAK1-TAB complexes in steady conditions. In turn, …

**Summary**, from NCBI Gene [11274](https://www.ncbi.nlm.nih.gov/gene/11274):

> The protein encoded by this gene belongs to the ubiquitin-specific proteases (UBP) family of enzymes that cleave ubiquitin from ubiquitinated protein substrates. It is highly expressed in liver and thymus, and is localized to the nucleus. This protein efficiently cleaves only ISG15 (a ubiquitin-like protein) fusions, and deletion of this gene in mice results in a massive increase of ISG15 conjugates in tissues, indicating that this protein is a major ISG15-specific protease. Mice lacking this …

**Accessions** — [HGNC:12616](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12616) · Entrez [11274](https://www.ncbi.nlm.nih.gov/gene/11274) · UniProt [Q9UMW8](https://www.uniprot.org/uniprotkb/Q9UMW8) · Ensembl [ENSG00000184979](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184979)

## Data

Gene col 11598: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11598); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11598, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11598]; `tensor/DDL_lfc|DDL_z.npy` [11598]; `embed/gene_vectors.npy` [11598]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11598 or target_col == 11598). Every well: [[USP18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USP18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
