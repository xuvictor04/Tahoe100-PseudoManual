---
symbol: "CDRT4"
type: "gene"
col: 14207
ensembl_id: "ENSG00000239704"
name: "CMT1A duplicated region transcript 4"
location: "17p12"
module: 56
arm: "+"
pooled_cpm: 26.51
n_lines_expressing: 48
n_dd_up: 1
n_dd_down: 26
n_dd_up_clean: 1
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# CDRT4

*CMT1A duplicated region transcript 4* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.37× (z +4.1, q 0.028, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (19 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.495× (z -12.8, q 2e-34, down in 38 of 45 measured lines) ⚠ cell-cycle shift, explains ~61% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.587× (z -9.7, q 4e-20, down in 32 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TVP23C-CDRT4]] (+0.92, fdr 7e-06, ⚠ same locus), [[TVP23C]] (+0.76, fdr 7e-06, ⚠ same locus), [[MINAR1]] (+0.64, fdr 1e-05), [[IL20RB]] (+0.64, fdr 1e-05), [[TMED3]] (+0.63, fdr 7e-06); moves opposite to [[SINHCAF]] (-0.57, fdr 1e-05), [[THAP12]] (-0.53, fdr 3e-05), [[MAP3K1]] (-0.52, fdr 3e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LYG1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14207.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.028 | 22/46 (LoVo, HT-29, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.20× | +3.3 | 0.23 | 14/46 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 1.60× | +3.1 | 0.23 | 8/46 (SW480, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | 1.27× | +3.1 | 0.23 | 13/46 (SW48, A549, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~95% of this change | 1.27× | +3.1 | 0.23 | 12/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 19 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14207.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.495×** | -12.8 | 2e-34 | 38/45 (A-172, A549, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.312×** | -12.3 | 2e-32 | 37/45 (A498, PANC-1, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.401×** | -11.7 | 2e-29 | 37/45 (KATO III, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.450×** | -10.3 | 2e-22 | 36/46 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.587×** | -9.7 | 4e-20 | 32/44 (H4, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.458×** | -9.3 | 2e-18 | 27/35 (NCI-H460, HS-578T, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change | **0.495×** | -9.0 | 1e-17 | 28/42 (HCT15, LoVo, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.279×** | -8.6 | 7e-16 | 39/46 (LS 180, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~23% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.449×** | -8.5 | 1e-15 | 38/43 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.528×** | -8.2 | 1e-14 | 29/46 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.541×** | -7.9 | 2e-13 | 33/46 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.378×** | -6.5 | 3e-09 | 26/44 (A-172, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.603×** | -6.5 | 3e-09 | 29/46 (KATO III, PANC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | **0.549×** | -6.3 | 9e-09 | 21/32 (NCI-H460, HCT15, …) | all doses, flat | composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.663×** | -5.3 | 5e-06 | 25/46 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.008 | 18/46 (A549, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.751×** | -3.4 | 0.017 | 15/45 (H4, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.628×** | -3.1 | 0.039 | 15/45 (A-172, HCT15, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.37 per unit of S-phase module lfc, -0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14207. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.1 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -11.5) |
| [[A-172 (line)]] | wt | 36.6 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -20.6) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.151× (z -14.3) |
| [[A498 (line)]] | wt | 44.7 | 0 | 8 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -15.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.202× (z -11.5) |
| [[A549 (line)]] | wt | 41.3 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -16.4) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.187× (z -11.6) |
| [[KATO III (line)]] | alt | 31.0 | 0 | 7 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0578× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[PANC-1 (line)]] | alt | 12.5 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -15.9) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.291× (z -9.4) |
| [[H4 (line)]] | wt | 39.4 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.228× (z -11.9) |
| [[HS-578T (line)]] | alt | 44.5 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0964× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -9.8) |
| [[LS 180 (line)]] | wt | 27.8 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -11.5) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0682× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 21.3 | 0 | 5 (5 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.102× (z -15.4) ⚠ cell-cycle shift, explains ~44% of this change |
| [[CFPAC-1 (line)]] | alt | 28.7 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -13.7) ⚠ cell-cycle shift, explains ~61% of this change |
| [[HOP62 (line)]] | alt | 54.6 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.112× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -8.6) |
| [[SNU-423 (line)]] | alt | 32.4 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.8) ⚠ cell-cycle shift, explains ~61% of this change · without an alert: [[Hydroxyurea (drug)]] 0.05 µM 0.133× (z -12.0) |
| [[HCT15 (line)]] | alt | 80.6 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0600× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[J82 (line)]] | alt | 30.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.232× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.403× (z -9.4) |
| [[LoVo (line)]] | wt | 47.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[A-427 (line)]] | wt | 12.5 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -11.6) |
| [[NCI-H1792 (line)]] | alt | 20.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.144× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 21.2 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.156× (z -13.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.120× (z -8.5) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 19.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0599× (z -8.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0607× (z -11.9) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.202× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H23 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -10.2) ⚠ cell-cycle shift, explains ~61% of this change |
| [[Panc 03.27 (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.185× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[RKO (line)]] | wt | 36.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -8.6) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 28.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~74% of this change |
| [[SW 1271 (line)]] | alt | 64.1 | 0 | 1 | — | [[Decitabine (drug)]] 0.5 µM 0.0898× (z -8.7) |
| [[SW 900 (line)]] | alt | 21.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0834× (z -10.9) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.86 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14207), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TVP23C-CDRT4]] | +0.92 | +0.91 / +0.92 | both halves | 7e-06 | STRING 737; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[TVP23C]] | +0.76 | +0.73 / +0.77 | both halves | 7e-06 | STRING 742; ⚠ same locus (26.5 kb, same strand: neighbours can correlate without regulation) |
| [[MINAR1]] | +0.64 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[IL20RB]] | +0.64 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[TMED3]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[APRG1]] | +0.63 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[LINC02804]] | +0.62 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ASIC4]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[KCNQ1OT1]] | +0.59 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[TICAM2]] | +0.59 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[RPS6KC1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[POFUT2]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PGM3]] | +0.57 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TTN-AS1]] | +0.57 | +0.38 / +0.61 | both halves | 7e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SINHCAF]] | -0.57 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[THAP12]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[MAP3K1]] | -0.52 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[RNF138]] | -0.51 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[YAP1]] | -0.49 | -0.38 / -0.50 | both halves | 7e-05 |  |
| [[COX20]] | -0.47 | -0.38 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LYG1]] | B | LYG1 activity raises CDRT4's level | lines that do not express LYG1 (5) vs lines expressing it (45) | 2.90× lower at baseline in the lines without LYG1 | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02133, RBM44, DIRC3-AS1; maybe low, not absent |
| [[LINC01422]] | B | LINC01422 activity raises CDRT4's level | lines that do not express LINC01422 (6) vs lines expressing it (44) | 1.57× lower at baseline in the lines without LINC01422 | 0.093 | ⚠ within organs, on part of the lines; also absent: ESRRB, MIAT, ARHGAP15 |
| [[RBM44]] | C | RBM44 activity raises CDRT4's level | lines that do not express RBM44 (3) vs lines expressing it (47) | 3.62× lower at baseline in the lines without RBM44 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC02133, LYG1, SYCP2L; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.564). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (19.1, -33.6); signed map (-55.9, 16.7). **Vector** length 83.3, 20.2% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.8 | +4.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.5 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | -2.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +2.4 | +1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.5 | -0.8 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.1 | -9.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.9 | -8.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.6 | -8.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.2 | -12.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -3.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -2.1 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | CMT1A duplicated region transcript 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p12 — chr17:15,436,015-15,475,728 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36674 |
| Matched by | ensembl_id |

UniProt [Q8N9R6](https://www.uniprot.org/uniprotkb/Q8N9R6) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:14383](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14383) · Entrez [284040](https://www.ncbi.nlm.nih.gov/gene/284040) · UniProt [Q8N9R6](https://www.uniprot.org/uniprotkb/Q8N9R6) · Ensembl [ENSG00000239704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239704)

## Data

Gene col 14207: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14207); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14207, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14207]; `tensor/DDL_lfc|DDL_z.npy` [14207]; `embed/gene_vectors.npy` [14207]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14207 or target_col == 14207). Every well: [[CDRT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDRT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
