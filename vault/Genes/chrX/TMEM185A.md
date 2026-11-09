---
symbol: "TMEM185A"
type: "gene"
col: 15626
ensembl_id: "ENSG00000269556"
name: "transmembrane protein 185A"
location: "Xq28"
module: 30
arm: "+"
pooled_cpm: 13.14
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 13
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# TMEM185A

*transmembrane protein 185A* — Xq28

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.80× (z +7.9, q 2e-12, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.493× (z -14.6, q 1e-45, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STX7]] (+0.75, fdr 7e-06), [[MRI1]] (+0.73, fdr 7e-06), [[ORC4]] (+0.72, fdr 7e-06); moves opposite to [[ERCC6L2]] (-0.71, fdr 7e-06), [[MPDU1]] (-0.68, fdr 1e-05), [[SLC20A2]] (-0.68, fdr 7e-06).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ABL1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +7.9 | 2e-12 | 31/48 (HT-29, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.59×** | +7.3 | 1e-10 | 24/43 (LS 180, NCI-H460, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.40×** | +6.9 | 8e-10 | 30/48 (AsPC-1, RKO, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.57×** | +6.6 | 7e-09 | 28/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.4 | 2e-08 | 26/48 (J82, A498, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +6.0 | 1e-07 | 23/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +5.3 | 1e-05 | 21/48 (LOX-IMVI, HepG2/C3A, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.0 | 0.004 | 15/48 (PANC-1, HT-29, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.30×** | +3.9 | 0.006 | 13/48 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.010 | 6/47 (HT-29, PANC-1, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.028 | 4/43 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.28×** | +3.4 | 0.030 | 13/39 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.25×** | +3.3 | 0.045 | 12/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | 1.17× | +3.2 | 0.057 | 4/48 (SNU-1, SHP-77, …) | top dose only |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.081 | 7/47 (KATO III, HT-29, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.493×** | -14.6 | 1e-45 | 34/45 (AsPC-1, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.591×** | -7.7 | 3e-12 | 25/33 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.579×** | -7.7 | 3e-12 | 20/25 (SW480, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.753×** | -5.9 | 7e-07 | 17/48 (CFPAC-1, A-172, …) | top dose only |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.699×** | -5.2 | 2e-05 | 20/48 (COLO 205, AsPC-1, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.725×** | -4.7 | 3e-04 | 18/47 (A-172, NCI-H2030, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.738×** | -4.1 | 0.003 | 12/28 (SNU-423, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -4.1 | 0.003 | 15/47 (NCI-H460, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.761×** | -4.0 | 0.004 | 21/45 (LOX-IMVI, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.755×** | -4.0 | 0.004 | 20/47 (A-172, SW480, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.829×** | -3.9 | 0.005 | 16/48 (CHP-212, LS 180, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.769×** | -3.8 | 0.006 | 13/48 (A498, KATO III, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.770×** | -3.8 | 0.006 | 14/48 (CFPAC-1, A498, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.783×** | -3.6 | 0.014 | 14/48 (SW 900, A498, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.794×** | -3.4 | 0.028 | 15/48 (A498, SW 900, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.035 | 4/48 (SW1417, A498, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.799×** | -3.3 | 0.035 | 7/48 (LOX-IMVI, SNU-1, …) | inconsistent across doses |  |
| [[Mifepristone (drug)]] 0.5 µM |  | **0.804×** | -3.2 | 0.042 | 6/47 (Panc 03.27, KATO III, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.665×** | -3.1 | 0.051 | 5/45 (hTERT-HPNE, RKO, …) | top dose only | noisy plate (z scaled) |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **0.810×** | -3.1 | 0.055 | 7/47 (SW 1271, HS-578T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 24.9 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -11.0) |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -10.3) |
| [[HS-578T (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.298× (z -8.6) |
| [[KATO III (line)]] | alt | 15.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0897× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 19.2 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.156× (z -15.3) |
| [[SK-MEL-2 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -12.3) |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -8.6) |
| [[SW 900 (line)]] | alt | 18.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.234× (z -10.7) |
| [[SW480 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -16.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.122× (z -16.3) |
| [[CFPAC-1 (line)]] | alt | 14.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -11.3) |
| [[COLO 205 (line)]] | alt | 7.48 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.05 µM 0.0602× (z -8.5) |
| [[H4 (line)]] | wt | 11.4 | 0 | 1 | — | [[Terfenadine (drug)]] 0.5 µM 0.0804× (z -9.2) |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0960× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 13.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -14.0) |
| [[LOX-IMVI (line)]] | wt | 9.93 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0790× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 8.68 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H460 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[RPMI-7951 (line)]] | alt | 11.8 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.103× (z -10.2) |
| [[SNU-1 (line)]] | wt | 12.1 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0768× (z -8.6) |
| [[SW1417 (line)]] | alt | 19.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -11.5) |
| [[A-427 (line)]] | wt | 9.03 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STX7]] | +0.75 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[MRI1]] | +0.73 | +0.60 / +0.65 | both halves | 7e-06 |  |
| [[ORC4]] | +0.72 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[RAB4A]] | +0.70 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[KBTBD3]] | +0.69 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[CAT]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[SLC9A6]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[C12orf76]] | +0.69 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[ZFP14]] | +0.69 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[USP30]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[NBPF3]] | +0.69 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.68 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERCC6L2]] | -0.71 | -0.72 / -0.58 | both halves | 7e-06 |  |
| [[MPDU1]] | -0.68 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[SLC20A2]] | -0.68 | -0.66 / -0.59 | both halves | 7e-06 |  |
| [[PCBP1-AS1]] | -0.66 | -0.61 / -0.57 | both halves | 9e-06 |  |
| [[HCG18]] | -0.66 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[SECISBP2]] | -0.64 | -0.63 / -0.41 | both halves | 4e-05 |  |
| [[SP2]] | -0.64 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ALG13]] | -0.63 | -0.44 / -0.56 | both halves | 3e-05 |  |
| [[IDI2-AS1]] | -0.62 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[LINC01934]] | -0.62 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[LANCL2]] | -0.61 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TSTD2]] | -0.61 | -0.49 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | ABL1 activity lowers TMEM185A's level | compounds that target ABL1: 4 of 6 raise it (Flumatinib, NG25, Ponatinib, Radotinib) | 67% of the class's compounds vs 3.4% of all compounds | 0.025 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.789). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (0.3, -7.8); signed map (-30.8, -8.7). **Vector** length 91.5, 18.8% of its response variance represented; |z| ≥ 3 in 925 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +5.2 | +6.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.6 | +6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | +3.8 | +6.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.6 | +3.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +4.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.5 | +7.3 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.4 | -14.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.4 | -5.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.9 | -2.7 |
|  | [[Thymol (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -2.1 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 185A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq28 — chrX:149,596,556-149,631,912 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CXorf13, FAM11A, FRAXF |
| Matched by | ensembl_id |

UniProt [Q8NFB2](https://www.uniprot.org/uniprotkb/Q8NFB2) carries no function annotation.

**Summary**, from NCBI Gene [84548](https://www.ncbi.nlm.nih.gov/gene/84548):

> The protein encoded by this gene is predicted to be a transmembrane protein. This gene is best known for localizing to the CpG island of the fragile site FRAXF. The 5' untranslated region of this gene contains a CGG trinucleotide repeat sequence that normally consists of 7-40 tandem CGG repeats but which can expand to greater than 300 repeats. Methylation of the CpG island leads to transcriptional silencing of this gene, but neither the silencing nor an expanded repeat region appear to manifest …

**Accessions** — [HGNC:17125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17125) · Entrez [84548](https://www.ncbi.nlm.nih.gov/gene/84548) · UniProt [Q8NFB2](https://www.uniprot.org/uniprotkb/Q8NFB2) · Ensembl [ENSG00000269556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269556)

## Data

Gene col 15626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15626); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15626]; `tensor/DDL_lfc|DDL_z.npy` [15626]; `embed/gene_vectors.npy` [15626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15626 or target_col == 15626). Every well: [[TMEM185A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM185A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
