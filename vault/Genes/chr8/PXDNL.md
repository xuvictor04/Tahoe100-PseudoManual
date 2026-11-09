---
symbol: "PXDNL"
type: "gene"
col: 7191
ensembl_id: "ENSG00000147485"
name: "peroxidasin like"
location: "8q11.22-q11.23"
module: 37
arm: "+"
pooled_cpm: 12.5
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# PXDNL

*peroxidasin like* — 8q11.22-q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.90× (z +21.9, q 0e+00, up in 44 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (14 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.464× (z -8.7, q 2e-15, down in 30 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.527× (z -7.2, q 6e-11, down in 27 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD7-DT]] (+0.80, fdr 7e-06), [[MCF2]] (+0.80, fdr 7e-06), [[ANKDD1B]] (+0.79, fdr 7e-06).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[STEAP1B]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.90×** | +21.9 | 0e+00 | 44/44 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.20×** | +11.5 | 3e-28 | 35/45 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +10.2 | 5e-22 | 35/46 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.74×** | +9.0 | 4e-17 | 29/48 (A-172, HOP62, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.55×** | +7.0 | 2e-10 | 30/48 (PANC-1, A498, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.69×** | +5.6 | 3e-06 | 14/28 (LoVo, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.60×** | +5.3 | 8e-06 | 25/47 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.58×** | +4.6 | 3e-04 | 8/20 (C32, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **2.11×** | +4.5 | 5e-04 | 16/46 (A498, HS-578T, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Filgotinib (drug)]] 5 µM |  | **1.47×** | +4.4 | 7e-04 | 20/48 (AsPC-1, SW 900, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.3 | 9e-04 | 15/47 (A498, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.0 | 0.003 | 6/48 (NCI-H23, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.42×** | +3.8 | 0.006 | 12/47 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.050 | 10/48 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.70×** | +3.2 | 0.057 | 5/47 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.464×** | -8.7 | 2e-15 | 30/45 (Panc 03.27, RPMI-7951, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.474×** | -8.5 | 8e-15 | 33/47 (HEC-1-A, NCI-H23, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.508×** | -7.7 | 3e-12 | 37/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.527×** | -7.2 | 6e-11 | 27/44 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.531×** | -7.2 | 9e-11 | 28/47 (RPMI-7951, LOX-IMVI, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.545×** | -6.9 | 6e-10 | 31/47 (LOX-IMVI, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.553×** | -6.7 | 2e-09 | 33/47 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.358×** | -6.1 | 8e-08 | 30/45 (NCI-H23, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.375×** | -5.8 | 4e-07 | 29/45 (HEC-1-A, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.565×** | -5.6 | 1e-06 | 24/46 (COLO 205, SW 900, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.388×** | -5.6 | 1e-06 | 27/48 (KATO III, SW 900, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **0.610×** | -5.6 | 1e-06 | 26/47 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.716×** | -5.3 | 4e-06 | 25/46 (NCI-H460, A549, …) | rises with dose | composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.525×** | -5.2 | 8e-06 | 24/48 (NCI-H23, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.422×** | -5.1 | 1e-05 | 22/40 (A549, A498, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.488×** | -4.3 | 7e-04 | 16/45 (SHP-77, HEC-1-A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.741×** | -3.4 | 0.022 | 7/47 (AsPC-1, SNU-423, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.565×** | -3.4 | 0.022 | 13/48 (LOX-IMVI, AN3 CA, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Pralsetinib (drug)]] 5 µM |  | **0.591×** | -3.1 | 0.048 | 9/43 (RKO, Hs 766T, …) | top dose only | noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.051 | 12/48 (NCI-H2030, AsPC-1, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.599×** | -3.0 | 0.055 | 11/45 (J82, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.690×** | -3.0 | 0.061 | 10/46 (HEC-1-A, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.83 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.53× (z +10.6) | [[Belinostat (drug)]] 0.5 µM 0.104× (z -10.0) |
| [[NCI-H460 (line)]] | wt | 26.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -12.3) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 12.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.42× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0799× (z -9.5) ⚠ toxic; cell-cycle shift, explains ~92% of this change |
| [[HOP62 (line)]] | alt | 13.7 | 2 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 10.1× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 31.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.211× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LS 180 (line)]] | wt | 5.63 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.89× (z +8.6) | [[Ligustrazine (drug)]] 5 µM 0.0629× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 6.46 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.37× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 5.95 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.28× (z +13.1) | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.105× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 7.47 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +10.5) | [[Digitoxin (drug)]] 5 µM 0.0617× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SNU-423 (line)]] | alt | 11.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +10.4) | [[Digitoxin (drug)]] 5 µM 0.137× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.71× (z +15.3) | — |
| [[A549 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 8.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +12.8) | — |
| [[BT-474 (line)]] | alt | 17.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.21× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 7.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.21× (z +10.4) | — |
| [[COLO 205 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0469× (z -10.9) ⚠ cell-cycle shift, explains ~52% of this change |
| [[HEC-1-A (line)]] | alt | 16.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +10.5) | — |
| [[HepG2_C3A (line)]] | wt | 8.17 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +11.0) | — |
| [[HS-578T (line)]] | alt | 19.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.91× (z +10.5) | — |
| [[HT-29 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0828× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[LoVo (line)]] | wt | 8.49 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.97× (z +11.6) | — |
| [[NCI-H23 (line)]] | alt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 6.46 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.34× (z +11.8) | — |
| [[RKO (line)]] | wt | 6.05 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +11.4) | — |
| [[RPMI-7951 (line)]] | alt | 26.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SHP-77 (line)]] | alt | 13.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.66× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.77× (z +9.5) | — |
| [[SW1417 (line)]] | alt | 4.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +10.0) | — |
| [[SW48 (line)]] | wt | 8.24 | 0 | 1 | — | [[Lopinavir (drug)]] 0.5 µM 0.0553× (z -8.5) |
| [[SW480 (line)]] | alt | 6.09 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.86× (z +10.0) | — |
| [[A-427 (line)]] | wt | 5.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.00 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | +0.80 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[MCF2]] | +0.80 | +0.74 / +0.71 | both halves | 7e-06 |  |
| [[ANKDD1B]] | +0.79 | +0.72 / +0.74 | both halves | 7e-06 |  |
| [[LINC02955]] | +0.78 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[C2orf88]] | +0.78 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[SLC6A13]] | +0.78 | +0.71 / +0.76 | both halves | 7e-06 |  |
| [[LINC02936]] | +0.77 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[CPEB2-DT]] | +0.77 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[PDC-AS1]] | +0.77 | +0.76 / +0.62 | both halves | 7e-06 |  |
| [[ZFHX2-AS1]] | +0.75 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[LINC02680]] | +0.74 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[HSD17B3]] | +0.74 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PXDNL's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SHROOM2]] | B | SHROOM2 activity lowers PXDNL's level | lines that do not express SHROOM2 (15) vs lines expressing it (35) | 1.33× higher at baseline in the lines without SHROOM2 | 0.044 | ⚠ within organs, on part of the lines; also absent: GPR143, RASGEF1C |
| [[C9]] | B | C9 activity raises PXDNL's level | lines that do not express C9 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without C9 | 0.077 | ⚠ within organs, on part of the lines; also absent: DAB2, ENSG00000253891, PTGFR |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STEAP1B]] | C | PXDNL's natural level weakens STEAP1B's drug response | PXDNL's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.64, reverse -0.25; direction not clear | 0.066 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| cells under [[Anethole trithione (drug)]] 0.5 µM | C | PXDNL's natural level raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | PXDNL's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.58 | 0.491 over the table, 0.098 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.722). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, -14.5); signed map (19.3, 2.5). **Vector** length 103, 24.7% of its response variance represented; |z| ≥ 3 in 1,133 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +12.5 | +21.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +9.7 | +11.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +10.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +9.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +4.0 | +3.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.0 | +4.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.9 | +4.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -5.7 | -7.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.6 | -7.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -5.1 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -4.7 | -8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.2 | -3.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -4.0 | -3.4 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.4 | -5.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.2 | -5.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -3.1 | -5.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.9 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | peroxidasin like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q11.22-q11.23 — chr8:51,319,577-51,809,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25471, PMR1 |
| Gene groups (HGNC) | I-set domain containing; Heme peroxidase family |
| Matched by | ensembl_id |

**Function**, from UniProt [A1KZ92](https://www.uniprot.org/uniprotkb/A1KZ92) (Probable oxidoreductase PXDNL):

> Probable oxidoreductase (Probable). Lacks peroxidase activity. Inhibits the peroxidase activity of PXDN through its interaction.; [Isoform PMR1]: Endonuclease selectively degrading some target mRNAs while they are engaged by translating ribosomes, among which albumin and beta-globin mRNAs.

**Summary**, from NCBI Gene [137902](https://www.ncbi.nlm.nih.gov/gene/137902):

> Predicted to enable heme binding activity and peroxidase activity. Predicted to be involved in hydrogen peroxide catabolic process. Located in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26359](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26359) · Entrez [137902](https://www.ncbi.nlm.nih.gov/gene/137902) · UniProt [A1KZ92](https://www.uniprot.org/uniprotkb/A1KZ92) · Ensembl [ENSG00000147485](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147485)

## Data

Gene col 7191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7191); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7191]; `tensor/DDL_lfc|DDL_z.npy` [7191]; `embed/gene_vectors.npy` [7191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7191 or target_col == 7191). Every well: [[PXDNL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXDNL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
