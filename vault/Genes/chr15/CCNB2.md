---
symbol: "CCNB2"
type: "gene"
col: 8073
ensembl_id: "ENSG00000157456"
name: "cyclin B2"
location: "15q22.2"
module: 22
arm: "+"
pooled_cpm: 28.41
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 25
n_dd_up_clean: 8
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCNB2

*cyclin B2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.79× (z +10.8, q 2e-24, up in 39 of 47 measured lines) ⚠ cell-cycle shift, would explain all of this change. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 1.40× (z +4.4, q 9e-04, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (15 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.566× (z -7.5, q 5e-11, down in 35 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KIF20A]] (+0.93, fdr 7e-06), [[NEK2]] (+0.93, fdr 7e-06), [[CCNB1]] (+0.93, fdr 7e-06).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PIMREG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8073.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.79×** | +10.8 | 2e-24 | 39/47 (PANC-1, A549, …) | top dose only | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | **1.84×** | +8.0 | 4e-13 | 35/47 (HOP62, HT-29, …) | all doses, flat | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **2.87×** | +7.2 | 8e-11 | 36/46 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **1.52×** | +5.5 | 5e-06 | 25/45 (NCI-H23, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **1.53×** | +5.4 | 9e-06 | 19/35 (A-172, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.46×** | +4.8 | 1e-04 | 28/48 (PANC-1, A549, …) | rises with dose | composition shift |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.29×** | +4.7 | 2e-04 | 26/48 (HT-29, A549, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.40×** | +4.4 | 9e-04 | 25/47 (HOP62, hTERT-HPNE, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.24×** | +4.0 | 0.004 | 21/48 (HT-29, HEC-1-A, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.38×** | +3.9 | 0.005 | 17/39 (PANC-1, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.33×** | +3.7 | 0.009 | 14/47 (HOP62, H4, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.35×** | +3.6 | 0.014 | 19/47 (HOP62, HT-29, …) | all doses, flat |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.015 | 17/48 (HT-29, KATO III, …) | rises with dose |  |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **1.21×** | +3.5 | 0.017 | 10/48 (Hs 766T, SW1417, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **1.67×** | +3.5 | 0.017 | 16/48 (HT-29, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 0.5 µM |  | **1.26×** | +3.1 | 0.078 | 9/47 (HT-29, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.090 | 11/47 (HOP62, NCI-H2030, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.090 | 15/48 (NCI-H460, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 15 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8073.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.566×** | -7.5 | 5e-11 | 35/47 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **0.575×** | -7.3 | 9e-11 | 31/47 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.576×** | -7.2 | 9e-11 | 35/48 (H4, LS 180, …) | all doses, stronger at high dose |  |
| [[Cytarabine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.597×** | -6.5 | 1e-08 | 33/47 (HEC-1-A, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.595×** | -6.4 | 1e-08 | 29/48 (HOP62, SHP-77, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.714×** | -6.3 | 4e-08 | 29/48 (LS 180, A498, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.674×** | -5.2 | 2e-05 | 26/47 (PANC-1, SW48, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~90% of this change | **0.712×** | -4.5 | 6e-04 | 28/48 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.714×** | -4.4 | 6e-04 | 21/47 (H4, LS 180, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **0.716×** | -4.4 | 7e-04 | 22/47 (A-172, LS 180, …) | two highest doses |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.793×** | -4.3 | 9e-04 | 20/48 (A-172, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~87% of this change | **0.735×** | -4.0 | 0.002 | 24/48 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.741×** | -3.9 | 0.004 | 21/47 (SHP-77, HCT15, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.746×** | -3.9 | 0.005 | 16/48 (NCI-H2030, A-427, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.749×** | -3.8 | 0.005 | 20/47 (NCI-H2030, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.759×** | -3.6 | 0.009 | 20/48 (SW1417, HT-29, …) | rises with dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | **0.744×** | -3.6 | 0.010 | 17/47 (SW48, HOP62, …) | all doses, flat |  |
| [[Cytarabine (drug)]] 0.05 µM |  | **0.758×** | -3.4 | 0.022 | 18/47 (NCI-H1573, HOP62, …) | all doses, stronger at high dose |  |
| [[Gemcitabine (drug)]] 0.05 µM |  | **0.826×** | -3.3 | 0.023 | 16/48 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.779×** | -3.2 | 0.042 | 10/47 (A498, SW48, …) | top dose only |  |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **0.791×** | -3.1 | 0.050 | 13/47 (A-172, A549, …) | inconsistent across doses |  |
| [[Cepharanthine (drug)]] 5 µM |  | 0.848× | -3.1 | 0.050 | 11/48 (SW 900, HEC-1-A, …) | top dose only |  |
| [[Rapamycin (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.087 | 11/47 (Hs 766T, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.42 per unit of S-phase module lfc, +1.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8073. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 39.3 | 0 | 3 (2 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0217× (z -18.2) ⚠ cell-cycle shift, explains ~92% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.238× (z -9.6) |
| [[LS 180 (line)]] | wt | 28.3 | 0 | 2 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.261× (z -10.6) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 28.7 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +13.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[A-172 (line)]] | wt | 21.9 | 0 | 1 | — | [[Amsacrine (drug)]] 5 µM 0.372× (z -9.2) |
| [[A498 (line)]] | wt | 24.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.377× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 35.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.15× (z +13.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 18.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.159× (z -9.1) |
| [[HOP62 (line)]] | alt | 34.1 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.65× (z +9.4) ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[Hs 766T (line)]] | wt | 18.2 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.102× (z -11.0) |
| [[HT-29 (line)]] | alt | 43.6 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 3.82× (z +9.0) ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[LoVo (line)]] | wt | 32.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +8.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 33.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +12.5) ⚠ cell-cycle shift, would explain all of this change | — |
| [[Panc 03.27 (line)]] | alt | 36.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +12.9) ⚠ cell-cycle shift, would explain all of this change | — |
| [[RKO (line)]] | wt | 25.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SHP-77 (line)]] | alt | 41.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.189× (z -9.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.238× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 40.9 | 1 (1 ⚠) | 0 | [[Docetaxel (drug)]] 0.05 µM 2.92× (z +8.5) ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | — |
| [[A-427 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 60.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8073), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KIF20A]] | +0.93 | +0.90 / +0.94 | both halves | 7e-06 | STRING 938 |
| [[NEK2]] | +0.93 | +0.93 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 902 |
| [[CCNB1]] | +0.93 | +0.89 / +0.94 | both halves | 7e-06 | same gene group; pathway: Activation of NIMA Kinases NEK9, NEK6, NEK7; STRING 998 |
| [[CKAP2]] | +0.92 | +0.90 / +0.92 | both halves | 7e-06 | STRING 578 |
| [[PLK1]] | +0.91 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 995 |
| [[DLGAP5]] | +0.91 | +0.88 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 974 |
| [[DEPDC1]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 724 |
| [[TPX2]] | +0.90 | +0.89 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 953 |
| [[CCNA2]] | +0.90 | +0.85 / +0.92 | both halves | 7e-06 | same gene group; pathway: HALLMARK_G2M_CHECKPOINT; STRING 965 |
| [[TOP2A]] | +0.90 | +0.90 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 975 |
| [[KIF18A]] | +0.90 | +0.88 / +0.88 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints; STRING 809 |
| [[AURKA]] | +0.89 | +0.92 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 988 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIMREG]] | B | PIMREG activity raises CCNB2's level | lines that do not express PIMREG (6) vs lines expressing it (44) | 1.98× lower at baseline in the lines without PIMREG | 0.006 | ⚠ within organs, on part of the lines; also absent: PBK, AURKB, ENSG00000197332; maybe low, not absent |
| [[NEURL1B]] | B | NEURL1B activity raises CCNB2's level | lines that do not express NEURL1B (7) vs lines expressing it (43) | 1.68× lower at baseline in the lines without NEURL1B | 0.049 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131 |
| [[NEURL1B]] | B | NEURL1B activity strengthens CCNB2's drug response | lines that do not express NEURL1B (7) vs lines expressing it (41) | the lines without NEURL1B respond 0.65× as strongly (z diff +1.12); strongest at Bortezomib 0.05 µM: 0.99x vs 0.58x (z diff +3.0) | 0.096 | ⚠ within organs, on part of the lines; also absent: PIMREG, WNT9A, ENSG00000267131; target measured in part of the lines; artifact flags |
| [[PBK]] | C | PBK activity raises CCNB2's level | lines that do not express PBK (4) vs lines expressing it (46) | 2.40× lower at baseline in the lines without PBK | 0.008 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |
| [[NDC80]] | C | NDC80 activity raises CCNB2's level | lines that do not express NDC80 (3) vs lines expressing it (47) | 2.10× lower at baseline in the lines without NDC80 | 0.018 | ⚠ few lines (3 vs 47); across organs; also absent: SH3BP5, DSCC1, KLF9; maybe low, not absent |
| [[AURKB]] | C | AURKB activity raises CCNB2's level | lines that do not express AURKB (4) vs lines expressing it (46) | 2.18× lower at baseline in the lines without AURKB | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[CDCA3]], [[SPDL1]] | C | CDCA3, SPDL1 activity raises CCNB2's level | lines that do not express CDCA3, SPDL1 (3) vs lines expressing them (47) | 2.51× lower at baseline in the lines without CDCA3, SPDL1 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TBC1D19, PBK, SNPH; maybe low, not absent; its own permutation p; co-absent genes |
| [[CDC20]] | C | CDC20 activity raises CCNB2's level | lines that do not express CDC20 (3) vs lines expressing it (47) | 1.92× lower at baseline in the lines without CDC20 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: SPDL1, ARHGAP10, CDC45; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.7, -57.1); signed map (-50.9, -43.2). **Vector** length 136, 43.0% of its response variance represented; |z| ≥ 3 in 1,108 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Mitotic Spindle Checkpoint* (reactome, mean cos +0.72 to 31); *Separation of Sister Chromatids* (reactome, mean cos +0.72 to 34); *Amplification  of signal from unattached  kinetochores via a MAD2  inhibitory signal* (reactome, mean cos +0.74 to 28).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +9.7 | +10.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~79% of this change | +6.7 | +8.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | +5.1 | +7.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.8 | +4.8 |
|  | [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | +3.9 | +4.7 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Mebendazole (drug)]] 0.5 µM |  | +2.3 | +3.1 |
|  | [[Peretinoin (drug)]] 0.05 µM |  | +2.2 | +3.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -7.8 | -7.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~68% of this change | -7.0 | -7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~77% of this change | -6.4 | -6.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~92% of this change | -5.2 | -7.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~88% of this change | -4.7 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.8 | -4.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -3.5 | -3.6 |
|  | [[EX229 (drug)]] 5 µM |  | -3.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cyclin B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:59,105,126-59,125,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HsT17299 |
| Gene groups (HGNC) | Cyclins; Centriolar satellite proteins |
| Hallmark sets | SPERMATOGENESIS, G2M_CHECKPOINT, MITOTIC_SPINDLE, E2F_TARGETS |
| Reactome | 24 pathways, smallest: G2/M DNA replication checkpoint; Activation of NIMA Kinases NEK9, NEK6, NEK7; Condensation of Prometaphase Chromosomes |
| Matched by | ensembl_id |

**Function**, from UniProt [O95067](https://www.uniprot.org/uniprotkb/O95067) (G2/mitotic-specific cyclin-B2):

> Essential for the control of the cell cycle at the G2/M (mitosis) transition.

**Summary**, from NCBI Gene [9133](https://www.ncbi.nlm.nih.gov/gene/9133):

> Cyclin B2 is a member of the cyclin family, specifically the B-type cyclins. The B-type cyclins, B1 and B2, associate with p34cdc2 and are essential components of the cell cycle regulatory machinery. B1 and B2 differ in their subcellular localization. Cyclin B1 co-localizes with microtubules, whereas cyclin B2 is primarily associated with the Golgi region. Cyclin B2 also binds to transforming growth factor beta RII and thus cyclin B2/cdc2 may play a key role in transforming growth factor …

**Accessions** — [HGNC:1580](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1580) · Entrez [9133](https://www.ncbi.nlm.nih.gov/gene/9133) · UniProt [O95067](https://www.uniprot.org/uniprotkb/O95067) · Ensembl [ENSG00000157456](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000157456)

## Data

Gene col 8073: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8073); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8073, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8073]; `tensor/DDL_lfc|DDL_z.npy` [8073]; `embed/gene_vectors.npy` [8073]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8073 or target_col == 8073). Every well: [[CCNB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCNB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
