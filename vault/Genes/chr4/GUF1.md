---
symbol: "GUF1"
type: "gene"
col: 7568
ensembl_id: "ENSG00000151806"
name: "GTP binding elongation factor GUF1"
location: "4p12"
module: 1
arm: "+"
pooled_cpm: 31.55
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 14
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# GUF1

*GTP binding elongation factor GUF1* — 4p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.76× (z +14.5, q 4e-45, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.712× (z -6.1, q 6e-07, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GTF2H3]] (+0.80, fdr 7e-06), [[MCCC2]] (+0.77, fdr 7e-06), [[MRRF]] (+0.76, fdr 7e-06); moves opposite to [[CARHSP1]] (-0.67, fdr 7e-06), [[RPL28]] (-0.67, fdr 7e-06), [[COX6A1]] (-0.67, fdr 7e-06).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PCSK1N]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 8 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7568.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.76×** | +14.5 | 4e-45 | 44/48 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.07×** | +12.7 | 1e-34 | 29/39 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.96×** | +12.2 | 4e-32 | 36/45 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.75×** | +10.2 | 2e-22 | 39/47 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.37×** | +8.1 | 5e-14 | 31/48 (NCI-H2347, A498, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.61×** | +8.1 | 6e-14 | 30/45 (A-427, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.43×** | +6.5 | 5e-09 | 32/47 (NCI-H2347, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +6.0 | 2e-07 | 26/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.30×** | +4.8 | 1e-04 | 21/48 (Hs 766T, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +4.2 | 0.002 | 21/48 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +3.8 | 0.007 | 17/47 (A549, A-172, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.23×** | +3.7 | 0.009 | 12/48 (A549, A-427, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.009 | 12/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.22×** | +3.5 | 0.017 | 15/47 (NCI-H1573, NCI-H2347, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.072 | 6/47 (AsPC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | 1.20× | +3.1 | 0.072 | 14/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.19× | +3.0 | 0.082 | 10/47 (NCI-H1792, RKO, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.38×** | +2.9 | 0.095 | 6/48 (MIA PaCa-2, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | 1.17× | +2.9 | 0.095 | 5/48 (A-427, SW480, …) | two highest doses | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | 1.17× | +2.9 | 0.095 | 6/47 (A498, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7568.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.712×** | -6.1 | 6e-07 | 28/47 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.734×** | -5.6 | 7e-06 | 25/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.753×** | -5.1 | 5e-05 | 21/47 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.818×** | -5.1 | 5e-05 | 24/48 (SK-MEL-2, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.764×** | -4.8 | 1e-04 | 22/48 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.761×** | -4.6 | 3e-04 | 25/48 (CHP-212, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.780×** | -4.5 | 7e-04 | 25/47 (LS 180, SW480, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.935× | -3.9 | 0.007 | 1/48 (Hs 766T) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.742×** | -3.8 | 0.008 | 19/47 (SNU-1, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -3.7 | 0.011 | 18/48 (PANC-1, H4, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.814×** | -3.7 | 0.011 | 19/47 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **0.814×** | -3.7 | 0.011 | 20/47 (SNU-1, LS 180, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.817×** | -3.6 | 0.012 | 17/48 (RKO, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.764×** | -3.5 | 0.022 | 11/48 (PANC-1, HS-578T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **0.833×** | -3.3 | 0.041 | 8/48 (SW480, SNU-1, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.715×** | -3.0 | 0.093 | 12/47 (RKO, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7568. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.8 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.47× (z +10.2) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.453× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.586× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 27.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) | — |
| [[HOP62 (line)]] | alt | 28.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +12.7) | — |
| [[LoVo (line)]] | wt | 36.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.03× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.08× (z +10.0) | — |
| [[LOX-IMVI (line)]] | wt | 25.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.46× (z +9.8) | — |
| [[NCI-H1792 (line)]] | alt | 24.5 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.39× (z +11.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.48× (z +8.8) | — |
| [[NCI-H23 (line)]] | alt | 44.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.9) | — |
| [[NCI-H2347 (line)]] | alt | 35.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.456× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~36% of this change |
| [[A-427 (line)]] | wt | 55.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.57× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 26.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.74× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 20.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.60× (z +10.5) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 43.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0997× (z -10.2) |
| [[HCT15 (line)]] | alt | 41.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 34.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.66× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.11× (z +8.9) | — |
| [[hTERT-HPNE (line)]] | wt | 23.3 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.127× (z -11.6) |
| [[KATO III (line)]] | alt | 29.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 33.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 8.75 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0719× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 27.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.9) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 65.3 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 27.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -9.9) |
| [[SNU-423 (line)]] | alt | 30.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.43× (z +10.2) | — |
| [[SW48 (line)]] | wt | 43.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.165× (z -10.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 47.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 41.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 49.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 24.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7568), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GTF2H3]] | +0.80 | +0.81 / +0.80 | both halves | 7e-06 |  |
| [[MCCC2]] | +0.77 | +0.79 / +0.71 | both halves | 7e-06 |  |
| [[MRRF]] | +0.76 | +0.63 / +0.79 | both halves | 7e-06 | STRING 688 |
| [[HDHD2]] | +0.75 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[IMPACT]] | +0.75 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.74 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[MBTPS2]] | +0.73 | +0.58 / +0.77 | both halves | 7e-06 |  |
| [[GMFB]] | +0.72 | +0.60 / +0.74 | both halves | 7e-06 |  |
| [[TRUB1]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[ICE2]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[UTP15]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[ALG10B]] | +0.70 | +0.62 / +0.68 | both halves | 7e-06 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARHSP1]] | -0.67 | -0.58 / -0.71 | both halves | 7e-06 |  |
| [[RPL28]] | -0.67 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[COX6A1]] | -0.67 | -0.63 / -0.58 | both halves | 7e-06 |  |
| [[UBL5]] | -0.67 | -0.65 / -0.58 | both halves | 8e-06 |  |
| [[ULK1]] | -0.67 | -0.64 / -0.62 | both halves | 7e-06 |  |
| [[RPS21]] | -0.67 | -0.67 / -0.57 | both halves | 9e-06 |  |
| [[RABAC1]] | -0.66 | -0.61 / -0.64 | both halves | 7e-06 |  |
| [[RPLP2]] | -0.66 | -0.61 / -0.60 | both halves | 7e-06 |  |
| [[UBA52]] | -0.66 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[RNF122]] | -0.65 | -0.48 / -0.66 | both halves | 2e-05 |  |
| [[MACO1]] | -0.64 | -0.53 / -0.67 | both halves | 1e-05 |  |
| [[RPS29]] | -0.64 | -0.52 / -0.63 | both halves | 1e-05 | STRING 655 |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCSK1N]] | B | PCSK1N activity raises GUF1's level | lines that do not express PCSK1N (21) vs lines expressing it (29) | 1.09× lower at baseline in the lines without PCSK1N | 0.005 | ⚠ within organs, on part of the lines; also absent: MAP6, CERS4, CACNG4 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.724). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-30.3, -16.9); signed map (-0.0, -37.6). **Vector** length 115, 28.7% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.9 | +10.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.4 | +14.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +12.7 |
|  | [[Selinexor (drug)]] 5 µM |  | +6.3 | +8.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.0 | +4.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.3 | +2.6 |
|  | [[EX229 (drug)]] 5 µM |  | +3.3 | +2.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.8 | +2.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.5 | -5.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -3.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.1 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.9 | -6.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.9 | -4.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | -3.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.5 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | GTP binding elongation factor GUF1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p12 — chr4:44,678,420-44,700,928 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ13220 |
| Gene groups (HGNC) | Translational GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N442](https://www.uniprot.org/uniprotkb/Q8N442) (Translation factor GUF1, mitochondrial):

> Promotes mitochondrial protein synthesis. May act as a fidelity factor of the translation reaction, by catalyzing a one-codon backward translocation of tRNAs on improperly translocated ribosomes. Binds to mitochondrial ribosomes in a GTP-dependent manner.

**Summary**, from NCBI Gene [60558](https://www.ncbi.nlm.nih.gov/gene/60558):

> This gene encodes a GTPase that triggers back-translocation of the elongating ribosome during mitochondrial protein synthesis. The protein contains a highly conserved C-terminal domain not found in other GTPases that facilitates tRNA binding. The encoded protein is thought to prevent misincorporation of amino acids in stressful, suboptimal conditions. An allelic variant in this gene has been associated with early infantile epileptic encephalopathy-40. Alternative splicing results in multiple …

**Accessions** — [HGNC:25799](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25799) · Entrez [60558](https://www.ncbi.nlm.nih.gov/gene/60558) · UniProt [Q8N442](https://www.uniprot.org/uniprotkb/Q8N442) · Ensembl [ENSG00000151806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151806)

## Data

Gene col 7568: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7568); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7568, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7568]; `tensor/DDL_lfc|DDL_z.npy` [7568]; `embed/gene_vectors.npy` [7568]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7568 or target_col == 7568). Every well: [[GUF1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUF1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
