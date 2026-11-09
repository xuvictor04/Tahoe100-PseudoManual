---
symbol: "TMX3"
type: "gene"
col: 9318
ensembl_id: "ENSG00000166479"
name: "thioredoxin related transmembrane protein 3"
location: "18q22.1"
module: 4
arm: "+"
pooled_cpm: 62.73
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 3
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# TMX3

*thioredoxin related transmembrane protein 3* — 18q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.55× (z +22.1, q 0e+00, up in 45 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.42× (z +8.3, q 1e-14, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.721× (z -10.9, q 5e-25, down in 31 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (J82 0.434×, NCI-H460 0.554×, LoVo 0.486×, PANC-1 0.572×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.547×, KATO III 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.561×, NCI-H23 0.554×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (H4 0.115×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0701×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[XRCC5]] (+0.74, fdr 7e-06), [[TMEM33]] (+0.73, fdr 7e-06), [[NUP155]] (+0.72, fdr 7e-06); moves opposite to [[WIPF2]] (-0.73, fdr 7e-06), [[INAFM1]] (-0.72, fdr 7e-06), [[CDKN2D]] (-0.71, fdr 7e-06).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 11 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9318.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.55×** | +22.1 | 0e+00 | 45/48 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.61×** | +21.8 | 0e+00 | 38/44 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +13.6 | 6e-40 | 38/45 (NCI-H1792, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.42×** | +8.3 | 1e-14 | 31/48 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.41×** | +7.6 | 4e-12 | 34/48 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +7.2 | 6e-11 | 30/48 (NCI-H1573, COLO 205, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.23×** | +7.0 | 2e-10 | 26/48 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.9 | 2e-07 | 21/36 (HS-578T, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.26×** | +5.3 | 8e-06 | 23/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.26×** | +5.3 | 8e-06 | 19/48 (HS-578T, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.26×** | +5.3 | 8e-06 | 22/47 (C32, NCI-H1792, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.24×** | +5.1 | 2e-05 | 23/48 (C32, LOX-IMVI, …) | top dose only |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +4.6 | 2e-04 | 19/48 (A498, HOP62, …) | inconsistent across doses |  |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.004 | 14/48 (Hs 766T, CFPAC-1, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 1.18× | +3.9 | 0.004 | 10/48 (hTERT-HPNE, H4, …) | inconsistent across doses |  |
| [[Belzutifan (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.005 | 13/47 (NCI-H23, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.17× | +3.5 | 0.017 | 16/47 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | 1.15× | +3.3 | 0.025 | 14/48 (H4, A498, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 1.14× | +3.2 | 0.040 | 8/48 (HEC-1-A, A-427, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 1.14× | +3.1 | 0.051 | 5/48 (HEC-1-A, H4, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | 1.13× | +2.9 | 0.082 | 12/45 (RPMI-7951, HCT15, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.09× | +2.9 | 0.093 | 7/48 (NCI-H1792, HS-578T, …) | top dose only |  |
| [[Larotrectinib (drug)]] 5 µM |  | 1.09× | +2.8 | 0.093 | 2/48 (SNU-1, HS-578T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9318.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 4 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 8 lines (J82 0.434×, NCI-H460 0.554×, LoVo 0.486×, PANC-1 0.572×, …); [[Ouabain (Octahydrate) (drug)]] 5 µM in 2 lines (PANC-1 0.547×, KATO III 0.408×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (PANC-1 0.561×, NCI-H23 0.554×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Sonidegib (drug)]] 5 µM in 1 line (H4 0.115×); [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM in 1 line (SW 1088 0.0701×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -10.9 | 5e-25 | 31/48 (J82, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Verteporfin (drug)]] 5 µM |  | **0.779×** | -5.7 | 4e-06 | 27/48 (A-427, C-33 A, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.818×** | -4.8 | 4e-04 | 20/48 (PANC-1, AN3 CA, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.867× | -3.4 | 0.11 | 18/48 (PANC-1, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9318. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 77.2 | 3 (3 ⚠) | 4 (3 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.66× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.572× (z -12.4) |
| [[NCI-H2347 (line)]] | alt | 47.8 | 4 (4 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +9.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SNU-423 (line)]] | alt | 42.9 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +12.8) ⚠ toxic; transcription drop · without an alert: [[Selinexor (drug)]] 5 µM 2.01× (z +9.2) | — |
| [[A498 (line)]] | wt | 57.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.17× (z +14.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.577× (z -10.1) |
| [[CFPAC-1 (line)]] | alt | 31.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.87× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 38.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.38× (z +15.2) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 56.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.34× (z +11.3) ⚠ toxic; transcription drop | — |
| [[HS-578T (line)]] | alt | 78.6 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +14.6) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 82.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.35× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.7) |
| [[LoVo (line)]] | wt | 51.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -12.4) |
| [[LOX-IMVI (line)]] | wt | 111 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.02× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.568× (z -10.9) |
| [[NCI-H1573 (line)]] | alt | 39.2 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.47× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 98.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +16.9) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 44.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.58× (z +11.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 66.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.554× (z -12.8) |
| [[A549 (line)]] | wt | 49.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +13.2) ⚠ toxic; transcription drop | — |
| [[HT-29 (line)]] | alt | 40.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.8) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.44× (z +11.4) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 73.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 42.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +11.5) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 93.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.471× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 55.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.6) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 26.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.28× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -8.6) |
| [[SW480 (line)]] | alt | 45.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.21× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 33.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.99× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 84.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +10.1) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.205× (z -8.6) ⚠ cell-cycle shift, explains ~25% of this change |
| [[C32 (line)]] | wt | 52.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +10.8) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 86.7 | 0 | 1 | — | [[Sonidegib (drug)]] 5 µM 0.115× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 102 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.56× (z +10.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.35× (z +10.3) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 59.7 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.408× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 149 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.554× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW 1088 (line)]] | alt | 75.4 | 0 | 1 | — | [[L-Eflornithine (monohydrochloride) (drug)]] 0.05 µM 0.0701× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 164 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 72.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 70.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 42.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 93.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 85.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 61.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9318), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[XRCC5]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[TMEM33]] | +0.73 | +0.67 / +0.74 | both halves | 7e-06 |  |
| [[NUP155]] | +0.72 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[NAA50]] | +0.71 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[CCT5]] | +0.71 | +0.73 / +0.66 | both halves | 7e-06 |  |
| [[CCT2]] | +0.69 | +0.64 / +0.77 | both halves | 7e-06 |  |
| [[FUCA2]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MACROH2A1]] | +0.67 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CCT3]] | +0.67 | +0.73 / +0.65 | both halves | 7e-06 |  |
| [[PTPN11]] | +0.67 | +0.58 / +0.70 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[PSMD1]] | +0.66 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[CHCHD3]] | +0.66 | +0.65 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WIPF2]] | -0.73 | -0.59 / -0.77 | both halves | 7e-06 |  |
| [[INAFM1]] | -0.72 | -0.65 / -0.67 | both halves | 7e-06 |  |
| [[CDKN2D]] | -0.71 | -0.65 / -0.76 | both halves | 7e-06 |  |
| [[GPX4]] | -0.69 | -0.65 / -0.68 | both halves | 7e-06 |  |
| [[ZFAND2B]] | -0.69 | -0.56 / -0.70 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.68 | -0.68 / -0.60 | both halves | 7e-06 |  |
| [[MED19]] | -0.68 | -0.50 / -0.67 | both halves | 1e-05 |  |
| [[TTC21A]] | -0.67 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[ARID3A]] | -0.66 | -0.60 / -0.65 | both halves | 7e-06 |  |
| [[ING2]] | -0.66 | -0.50 / -0.70 | both halves | 1e-05 |  |
| [[SNHG9]] | -0.65 | -0.60 / -0.67 | both halves | 7e-06 |  |
| [[SAT2]] | -0.65 | -0.66 / -0.58 | both halves | 7e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity lowers TMX3's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without BIK | 0.019 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[OVOL1]] | B | OVOL1 activity lowers TMX3's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 1.49× higher at baseline in the lines without OVOL1 | 0.045 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[PFN2]] | C | PFN2 activity raises TMX3's level | lines that do not express PFN2 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without PFN2 | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.738). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-23.7, -30.8); signed map (-13.0, -44.4). **Vector** length 113, 29.0% of its response variance represented; |z| ≥ 3 in 919 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Folding of actin by CCT/TriC* (reactome, mean cos +0.62 to 4); *Prefoldin mediated transfer of substrate  to CCT/TriC* (reactome, mean cos +0.53 to 5); *Cooperation of Prefoldin and TriC/CCT  in actin and tubulin folding* (reactome, mean cos +0.53 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.9 | +8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.7 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.2 | +13.6 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.8 | +7.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +21.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +3.1 | +3.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +5.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.6 | +3.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -10.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.7 | -2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.8 | -1.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | -3.2 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -0.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.1 | -2.7 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -3.0 | -2.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -5.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.0 | -1.4 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | thioredoxin related transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q22.1 — chr18:68,673,688-68,715,108 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20793, KIAA1830, PDIA13; previously TXNDC10 |
| Gene groups (HGNC) | Protein disulfide isomerases; Thioredoxin domain containing |
| Reactome | 4 pathways, smallest: Platelet degranulation; Response to elevated platelet cytosolic Ca2+; Platelet activation, signaling and aggregation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96JJ7](https://www.uniprot.org/uniprotkb/Q96JJ7) (Protein disulfide-isomerase TMX3):

> Probable disulfide isomerase, which participates in the folding of proteins containing disulfide bonds. May act as a dithiol oxidase. Acts as a regulator of endoplasmic reticulum-mitochondria contact sites via its ability to regulate redox signals.

**Summary**, from NCBI Gene [54495](https://www.ncbi.nlm.nih.gov/gene/54495):

> This gene encodes a member of the disulfide isomerase (PDI) family of endoplasmic reticulum (ER) proteins that catalyze protein folding and thiol-disulfide interchange reactions. The canonical protein encoded by this gene has an N-terminal ER-signal sequence, a catalytically active thioredoxin domain, one transmembrane domain and a C-terminal ER-retention sequence. This gene is expressed in many tissues but has its highest expression in heart and skeletal muscle. It is expressed in the retinal …

**Accessions** — [HGNC:24718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24718) · Entrez [54495](https://www.ncbi.nlm.nih.gov/gene/54495) · UniProt [Q96JJ7](https://www.uniprot.org/uniprotkb/Q96JJ7) · Ensembl [ENSG00000166479](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166479)

## Data

Gene col 9318: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9318); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9318, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9318]; `tensor/DDL_lfc|DDL_z.npy` [9318]; `embed/gene_vectors.npy` [9318]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9318 or target_col == 9318). Every well: [[TMX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
