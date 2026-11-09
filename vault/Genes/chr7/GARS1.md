---
symbol: "GARS1"
type: "gene"
col: 2724
ensembl_id: "ENSG00000106105"
name: "glycyl-tRNA synthetase 1"
location: "7p14.3"
module: 63
arm: "+"
pooled_cpm: 338.12
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 16
n_dd_up_clean: 28
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# GARS1

*glycyl-tRNA synthetase 1* — 7p14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.37× (z +14.2, q 7e-43, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.616× (z -7.6, q 2e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SARS1]] (+0.88, fdr 7e-06), [[ASNS]] (+0.88, fdr 7e-06), [[CARS1]] (+0.88, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HSPA9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2724.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.37×** | +14.2 | 7e-43 | 47/48 (LoVo, A-172, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.16×** | +8.6 | 2e-15 | 42/47 (COLO 205, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.98×** | +8.0 | 3e-13 | 47/48 (NCI-H2030, C-33 A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +7.1 | 2e-10 | 46/48 (C-33 A, PANC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM |  | **1.53×** | +6.6 | 3e-09 | 39/48 (SNU-1, BT-474, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.49×** | +6.3 | 3e-08 | 42/49 (COLO 205, CFPAC-1, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.46×** | +6.0 | 1e-07 | 40/48 (C-33 A, NCI-H2030, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.23×** | +4.9 | 7e-05 | 46/48 (LOX-IMVI, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.08×** | +4.4 | 5e-04 | 44/48 (AsPC-1, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **2.06×** | +4.4 | 6e-04 | 44/48 (NCI-H2030, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.45×** | +4.4 | 7e-04 | 33/48 (NCI-H23, COLO 205, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +4.0 | 0.003 | 34/48 (C-33 A, LOX-IMVI, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.003 | 34/48 (SNU-1, SHP-77, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +4.0 | 0.003 | 31/48 (SHP-77, SW 900, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +4.0 | 0.003 | 30/48 (LoVo, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.46×** | +3.9 | 0.003 | 31/48 (Hs 766T, BT-474, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.003 | 35/48 (SW 900, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2724.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.616×** | -7.6 | 2e-11 | 35/48 (HT-29, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.679×** | -6.1 | 2e-07 | 39/49 (H4, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.706×** | -5.6 | 4e-06 | 39/48 (SW1417, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.662×** | -4.8 | 2e-04 | 33/48 (HT-29, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.656×** | -4.7 | 2e-04 | 35/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.660×** | -4.5 | 6e-04 | 32/47 (LoVo, H4, …) | all doses, flat | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.672×** | -4.5 | 6e-04 | 31/47 (HT-29, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.663×** | -4.3 | 0.001 | 30/48 (HT-29, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.706×** | -4.1 | 0.003 | 41/49 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.732×** | -3.7 | 0.014 | 27/48 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **0.735×** | -3.6 | 0.016 | 33/48 (SW48, SW1417, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.728×** | -3.4 | 0.038 | 30/48 (SW1417, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.753×** | -3.1 | 0.073 | 27/47 (RKO, SW1417, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.600×** | -3.1 | 0.073 | 27/50 (C-33 A, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.767×** | -3.1 | 0.073 | 24/48 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.773×** | -3.0 | 0.092 | 27/48 (NCI-H2347, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2724. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 617 | 1 | 14 (6 ⚠) | [[Auranofin (drug)]] 5 µM 3.35× (z +14.0) | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.4) |
| [[LoVo (line)]] | wt | 453 | 3 (1 ⚠) | 9 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.54× (z +17.9) | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -20.4) |
| [[PANC-1 (line)]] | alt | 678 | 2 (1 ⚠) | 8 (2 ⚠) | [[Auranofin (drug)]] 5 µM 2.04× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -20.1) |
| [[H4 (line)]] | wt | 758 | 1 | 8 (3 ⚠) | [[Auranofin (drug)]] 5 µM 2.38× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.3) |
| [[SW1417 (line)]] | alt | 412 | 1 | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.18× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.426× (z -13.5) |
| [[SW48 (line)]] | wt | 577 | 1 (1 ⚠) | 6 (2 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 3.02× (z +9.3) ⚠ toxic | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -12.2) |
| [[C-33 A (line)]] | alt | 225 | 6 (1 ⚠) | 0 | [[5-Azacytidine (drug)]] 5 µM 3.63× (z +12.6) | — |
| [[SNU-1 (line)]] | wt | 453 | 3 | 3 (1 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.23× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -12.6) |
| [[A-427 (line)]] | wt | 432 | 3 | 2 (1 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 2.26× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -13.7) |
| [[SW480 (line)]] | alt | 319 | 2 (1 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 2.97× (z +13.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.8) |
| [[KATO III (line)]] | alt | 558 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 291 | 3 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 3.67× (z +9.5) ⚠ cell-cycle shift, explains ~12% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.34× (z +8.8) | — |
| [[RKO (line)]] | wt | 385 | 1 | 2 | [[Auranofin (drug)]] 5 µM 4.32× (z +12.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.0) |
| [[A-172 (line)]] | wt | 465 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.98× (z +16.4) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.387× (z -9.4) ⚠ toxic |
| [[A498 (line)]] | wt | 528 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.50× (z +11.0) | [[Homoharringtonine (drug)]] 5 µM 0.497× (z -11.3) |
| [[AN3 CA (line)]] | alt | 235 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.76× (z +14.0) | — |
| [[AsPC-1 (line)]] | alt | 292 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 4.17× (z +14.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 2.77× (z +10.5) | — |
| [[BT-474 (line)]] | alt | 196 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.34× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 152 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.68× (z +15.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 4.26× (z +10.5) | — |
| [[Hs 766T (line)]] | wt | 328 | 2 (1 ⚠) | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.73× (z +11.4) | — |
| [[HS-578T (line)]] | alt | 403 | 1 | 1 | [[Auranofin (drug)]] 5 µM 2.42× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -12.5) |
| [[hTERT-HPNE (line)]] | wt | 269 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.52× (z +11.6) | — |
| [[NCI-H2030 (line)]] | alt | 230 | 2 | 0 | [[Neratinib (maleate) (drug)]] 0.5 µM 3.48× (z +10.0) | — |
| [[Panc 03.27 (line)]] | alt | 128 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.72× (z +12.4) | — |
| [[SHP-77 (line)]] | alt | 214 | 2 | 0 | [[Auranofin (drug)]] 5 µM 4.89× (z +16.2) | — |
| [[C32 (line)]] | wt | 166 | 1 | 0 | [[Auranofin (drug)]] 5 µM 9.91× (z +15.4) | — |
| [[HCT15 (line)]] | alt | 283 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.69× (z +10.8) | — |
| [[HEC-1-A (line)]] | alt | 266 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.56× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 186 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.07× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 147 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.21× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 210 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.84× (z +13.4) | — |
| [[LS 180 (line)]] | wt | 295 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.72× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 512 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.13× (z +9.7) | — |
| [[NCI-H1573 (line)]] | alt | 121 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.72× (z +9.1) ⚠ toxic | — |
| [[NCI-H23 (line)]] | alt | 266 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.19× (z +11.9) | — |
| [[NCI-H2347 (line)]] | alt | 347 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 456 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.13× (z +11.6) | — |
| [[SK-MEL-2 (line)]] | alt | 303 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.12× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 240 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.48× (z +13.8) | — |
| [[SW 1271 (line)]] | alt | 186 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.80× (z +8.5) | — |
| [[SW 900 (line)]] | alt | 233 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +13.6) | — |
| [[A549 (line)]] | wt | 221 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 186 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 227 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 199 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 267 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 318 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 513 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 408 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2724), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SARS1]] | +0.88 | +0.88 / +0.86 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 975 |
| [[ASNS]] | +0.88 | +0.87 / +0.86 | both halves | 7e-06 | STRING 850 |
| [[CARS1]] | +0.88 | +0.87 / +0.88 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 894 |
| [[AARS1]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cytosolic tRNA aminoacylation; STRING 983 |
| [[XPOT]] | +0.86 | +0.86 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[TRIB3]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[MARS1]] | +0.84 | +0.84 / +0.82 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 927 |
| [[IARS1]] | +0.84 | +0.86 / +0.83 | both halves | 7e-06 | pathway: Cytosolic tRNA aminoacylation; STRING 970 |
| [[PHGDH]] | +0.84 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SESN2]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CHAC1]] | +0.84 | +0.75 / +0.85 | both halves | 7e-06 |  |
| [[MTHFD2]] | +0.84 | +0.85 / +0.83 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises GARS1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.46× lower at baseline in the lines without ASNSP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[PSAT1]] | B | PSAT1 activity raises GARS1's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.53× lower at baseline in the lines without PSAT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[ANK2]] | B | ANK2 activity raises GARS1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without ANK2 | 0.046 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[CTH]] | B | CTH activity raises GARS1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without CTH | 0.089 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |
| [[ASNS]] | C | ASNS activity raises GARS1's level | lines that do not express ASNS (4) vs lines expressing it (46) | 2.08× lower at baseline in the lines without ASNS | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: PPEF1; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPA9]] | C | GARS1's natural level weakens HSPA9's drug response | GARS1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.05; direction not clear | 0.079 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.939). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 48.0); signed map (-13.2, 24.5). **Vector** length 162, 70.4% of its response variance represented; |z| ≥ 3 in 1,568 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.70 to 20); *unfolded protein response* (hallmark, mean cos +0.77 to 11); *Metabolism of amino acids and derivatives* (reactome, mean cos +0.73 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +12.3 | +14.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +9.6 | +7.1 |
|  | [[Artesunate (drug)]] 5 µM |  | +9.5 | +6.6 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.7 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.4 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.4 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.9 | +4.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.8 | +3.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -10.7 | -4.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -9.7 | -4.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.0 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.9 | -7.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -6.5 | -4.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.8 | -3.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.8 | -4.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | glycyl-tRNA synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p14.3 — chr7:30,580,533-30,634,033 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GlyRS, DSMAV, SMAD1; previously CMT2D, GARS |
| Gene groups (HGNC) | Aminoacyl tRNA synthetases, Class II |
| Reactome | 4 pathways, smallest: Mitochondrial tRNA aminoacylation; Cytosolic tRNA aminoacylation; tRNA Aminoacylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P41250](https://www.uniprot.org/uniprotkb/P41250) (Glycine--tRNA ligase):

> Catalyzes the ATP-dependent ligation of glycine to the 3'-end of its cognate tRNA, via the formation of an aminoacyl-adenylate intermediate (Gly-AMP). Also produces diadenosine tetraphosphate (Ap4A), a universal pleiotropic signaling molecule needed for cell regulation pathways, by direct condensation of 2 ATPs. Thereby, may play a special role in Ap4A homeostasis.

**Summary**, from NCBI Gene [2617](https://www.ncbi.nlm.nih.gov/gene/2617):

> This gene encodes glycyl-tRNA synthetase, one of the aminoacyl-tRNA synthetases that charge tRNAs with their cognate amino acids. The encoded enzyme is an (alpha)2 dimer which belongs to the class II family of tRNA synthetases. It has been shown to be a target of autoantibodies in the human autoimmune diseases, polymyositis or dermatomyositis. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:4162](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4162) · Entrez [2617](https://www.ncbi.nlm.nih.gov/gene/2617) · UniProt [P41250](https://www.uniprot.org/uniprotkb/P41250) · Ensembl [ENSG00000106105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106105)

## Data

Gene col 2724: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2724); `tables/drug_effects.parquet` (46 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2724, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2724]; `tensor/DDL_lfc|DDL_z.npy` [2724]; `embed/gene_vectors.npy` [2724]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2724 or target_col == 2724). Every well: [[GARS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GARS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
