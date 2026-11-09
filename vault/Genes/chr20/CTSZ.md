---
symbol: "CTSZ"
type: "gene"
col: 2082
ensembl_id: "ENSG00000101160"
name: "cathepsin Z"
location: "20q13.32"
module: 50
arm: "+"
pooled_cpm: 24.99
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 4
direction_downstream: 8
tags: ["gene", "module/050"]
generated_by: "tahoemap"
---

# CTSZ

*cathepsin Z* — 20q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.81× (z +26.8, q 0e+00, up in 32 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.15× (z +4.1, q 0.006, up in 9 of 40 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.00×, A498 3.90×, A-172 4.59×, PANC-1 4.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 6.83×, SW480 3.68×, A498 3.67×, A-172 4.27×, …; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.464× (z -21.8, q 0e+00, down in 38 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP9]] (+0.82, fdr 7e-06), [[SELENON]] (+0.80, fdr 7e-06), [[DHFR]] (+0.77, fdr 7e-06); moves opposite to [[MED19]] (-0.67, fdr 7e-06), [[SMIM26]] (-0.67, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[METTL23]] (-0.67, fdr 7e-06), [[ZNF503]] (-0.66, fdr 7e-06).
> It is in [[Module 050]], a single-armed module (Extracellular matrix organization).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TEAD2]] → it (grade B ⚠); 8 go from it, the strongest it → [[FLNA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2082.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 8 lines (SW480 5.00×, A498 3.90×, A-172 4.59×, PANC-1 4.30×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 7 lines (KATO III 6.83×, SW480 3.68×, A498 3.67×, A-172 4.27×, …; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.81×** | +26.8 | 0e+00 | 32/34 (SW480, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +25.6 | 0e+00 | 29/30 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.71×** | +18.5 | 0e+00 | 30/32 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +5.3 | 1e-05 | 9/23 (NCI-H2347, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.15× | +4.1 | 0.006 | 9/40 (NCI-H2030, A-172, …) | top dose only | position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.23×** | +3.8 | 0.013 | 7/40 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.016 | 13/40 (A-427, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~17% of this change | 1.18× | +3.3 | 0.072 | 16/37 (NCI-H2347, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2082.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.464×** | -21.8 | 0e+00 | 38/40 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.478×** | -14.2 | 2e-43 | 38/40 (NCI-H23, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.500×** | -13.9 | 1e-41 | 33/40 (NCI-H460, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.609×** | -9.9 | 4e-21 | 30/40 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -9.6 | 6e-20 | 27/39 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.692×** | -7.4 | 1e-11 | 28/40 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.698×** | -7.2 | 5e-11 | 26/40 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.714×** | -6.8 | 1e-09 | 24/39 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.774×** | -5.1 | 2e-05 | 19/39 (LoVo, HOP62, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.831×** | -3.5 | 0.026 | 10/40 (NCI-H460, HT-29, …) | inconsistent across doses | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | 0.745× | -3.1 | 0.10 | 3/40 (A549, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.749× | -3.0 | 0.11 | 9/38 (Hs 766T, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2082. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 25.7 | 3 (3 ⚠) | 4 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +17.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.389× (z -10.4) |
| [[A-172 (line)]] | wt | 56.2 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.59× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -11.2) |
| [[HOP62 (line)]] | alt | 31.1 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 4.50× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.204× (z -19.2) |
| [[NCI-H2347 (line)]] | alt | 29.3 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.78× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -13.9) |
| [[A498 (line)]] | wt | 41.2 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.90× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.397× (z -10.1) |
| [[AsPC-1 (line)]] | alt | 23.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.55× (z +9.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.1) |
| [[CFPAC-1 (line)]] | alt | 24.8 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.93× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.8) |
| [[NCI-H2030 (line)]] | alt | 46.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.33× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -12.7) |
| [[NCI-H460 (line)]] | wt | 38.2 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -19.5) |
| [[PANC-1 (line)]] | alt | 16.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.455× (z -10.4) |
| [[SNU-423 (line)]] | alt | 26.7 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.1) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.302× (z -8.9) |
| [[HS-578T (line)]] | alt | 33.5 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.99× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -8.8) |
| [[HT-29 (line)]] | alt | 38.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -19.2) |
| [[hTERT-HPNE (line)]] | wt | 20.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.192× (z -9.3) |
| [[KATO III (line)]] | alt | 27.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.83× (z +13.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 22.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.4) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.289× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 23.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +13.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -11.3) |
| [[Panc 03.27 (line)]] | alt | 24.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.5) |
| [[RKO (line)]] | wt | 26.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -14.0) |
| [[RPMI-7951 (line)]] | alt | 55.1 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -15.6) |
| [[SW1417 (line)]] | alt | 40.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.35× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.521× (z -8.9) |
| [[COLO 205 (line)]] | alt | 19.9 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.102× (z -11.3) |
| [[Hs 766T (line)]] | wt | 34.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.66× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.2) |
| [[J82 (line)]] | alt | 28.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +10.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.357× (z -11.6) |
| [[LoVo (line)]] | wt | 19.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.95× (z +11.9) ⚠ toxic; transcription drop | [[Belinostat (drug)]] 5 µM 0.333× (z -8.5) |
| [[LS 180 (line)]] | wt | 22.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.73× (z +9.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -12.6) |
| [[A-427 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.91× (z +12.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 15.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.64× (z +10.2) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 18.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 20.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -13.2) |
| [[SW 900 (line)]] | alt | 15.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.86× (z +8.9) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 17.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0602× (z -11.6) |
| [[AN3 CA (line)]] | alt | 5.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.13 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.15 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.93 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2082), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP9]] | +0.82 | +0.76 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[SELENON]] | +0.80 | +0.78 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[DHFR]] | +0.77 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[LAMP1]] | +0.73 | +0.59 / +0.70 | both halves | 7e-06 | STRING 578 |
| [[RPN1]] | +0.71 | +0.64 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[CRTAP]] | +0.71 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[PPT1]] | +0.70 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[EMC1]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[CERS2]] | +0.70 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[RPSA]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[MAN2B2]] | +0.69 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[NCSTN]] | +0.68 | +0.58 / +0.67 | both halves | 8e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED19]] | -0.67 | -0.67 / -0.61 | both halves | 7e-06 |  |
| [[SMIM26]] ⚠ | -0.67 | -0.54 / -0.62 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[METTL23]] | -0.67 | -0.61 / -0.65 | both halves | 7e-06 |  |
| [[ZNF503]] | -0.66 | -0.66 / -0.64 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.66 | -0.58 / -0.64 | both halves | 7e-06 |  |
| [[NKAP]] | -0.65 | -0.63 / -0.56 | both halves | 1e-05 |  |
| [[ZNF593]] | -0.65 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.65 | -0.52 / -0.71 | both halves | 1e-05 |  |
| [[MRPL46]] | -0.64 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[TIPRL]] | -0.64 | -0.62 / -0.63 | both halves | 7e-06 |  |
| [[RBMX2]] | -0.64 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[MRPS18C]] | -0.63 | -0.57 / -0.61 | both halves | 1e-05 |  |
| [[TRAPPC2B]] | -0.63 | -0.50 / -0.61 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TEAD2]] | B | TEAD2 activity raises CTSZ's level | lines that do not express TEAD2 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without TEAD2 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000197813, SLC6A16, FBXO17 |
| [[HDAC6]] | B | HDAC6 activity raises CTSZ's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[OLFML2A]] | B | OLFML2A activity raises CTSZ's level | lines that do not express OLFML2A (20) vs lines expressing it (30) | 1.37× lower at baseline in the lines without OLFML2A | 0.082 | ⚠ within organs, on part of the lines; also absent: GBX1, FMNL1-DT, SCN5A |
| [[MYL9]] | B | MYL9 activity raises CTSZ's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 1.77× lower at baseline in the lines without MYL9 | 0.085 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLNA]] | B | CTSZ activity raises FLNA's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSZ | 0.018 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[ATL3]] | B | CTSZ activity raises ATL3's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 2.19× lower at baseline in the lines without CTSZ | 0.023 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[NAXD]] | B | CTSZ activity lowers NAXD's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.31× higher at baseline in the lines without CTSZ | 0.028 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[ARPIN]] | B | CTSZ activity raises ARPIN's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.41× lower at baseline in the lines without CTSZ | 0.034 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[CERCAM]] | B | CTSZ activity raises CERCAM's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without CTSZ | 0.040 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[EIF4H]] | B | CTSZ activity raises EIF4H's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.14× lower at baseline in the lines without CTSZ | 0.062 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[GLB1]] | B | CTSZ activity raises GLB1's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.18× lower at baseline in the lines without CTSZ | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |
| [[HCFC1]] | B | CTSZ activity lowers HCFC1's level | lines that do not express CTSZ (8) vs lines expressing it (42) | 1.30× higher at baseline in the lines without CTSZ | 0.093 | ⚠ within organs, on part of the lines; also absent: LRRK1, CAV2, PIWIL4; maybe low, not absent |

## Where it sits

- **Module**: [[Module 050]] — Extracellular matrix organization; 92 genes; every member is in the + arm (projection on the module's main direction 0.754). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.0, -23.5); signed map (-23.6, -37.8). **Vector** length 85.0, 19.0% of its response variance represented; |z| ≥ 3 in 782 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.51 to 12); *Degradation of the extracellular matrix* (reactome, mean cos +0.50 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +11.2 | +25.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +10.5 | +26.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +10.3 | +18.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.2 | +1.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +4.2 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.4 | +4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +1.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -14.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -13.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.4 | -6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -21.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -1.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.3 | -0.9 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.3 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | cathepsin Z |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.32 — chr20:58,985,686-59,008,238 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CTSX |
| Gene groups (HGNC) | Cathepsins |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 13 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Cargo concentration in the ER; Lysosome Vesicle Biogenesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UBR2](https://www.uniprot.org/uniprotkb/Q9UBR2) (Cathepsin Z):

> Exhibits carboxy-monopeptidase as well as carboxy-dipeptidase activity. Capable of producing kinin potentiating peptides (By similarity).

**Summary**, from NCBI Gene [1522](https://www.ncbi.nlm.nih.gov/gene/1522):

> The protein encoded by this gene is a lysosomal cysteine proteinase and member of the peptidase C1 family. It exhibits both carboxy-monopeptidase and carboxy-dipeptidase activities. The encoded protein has also been known as cathepsin X and cathepsin P. This gene is expressed ubiquitously in cancer cell lines and primary tumors and, like other members of this family, may be involved in tumorigenesis. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:2547](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2547) · Entrez [1522](https://www.ncbi.nlm.nih.gov/gene/1522) · UniProt [Q9UBR2](https://www.uniprot.org/uniprotkb/Q9UBR2) · Ensembl [ENSG00000101160](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000101160)

## Data

Gene col 2082: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2082); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2082, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2082]; `tensor/DDL_lfc|DDL_z.npy` [2082]; `embed/gene_vectors.npy` [2082]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2082 or target_col == 2082). Every well: [[CTSZ — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTSZ.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
