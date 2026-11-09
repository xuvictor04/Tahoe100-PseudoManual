---
symbol: "DNASE1"
type: "gene"
col: 13147
ensembl_id: "ENSG00000213918"
name: "deoxyribonuclease 1"
location: "16p13.3"
module: 80
arm: "+"
pooled_cpm: 29.93
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 20
n_dd_up_clean: 12
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# DNASE1

*deoxyribonuclease 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.27× (z +26.9, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (6 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.501× (z -11.1, q 1e-25, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBE3B]] (+0.71, fdr 1e-05), [[ARID4B]] (+0.70, fdr 7e-06), [[NIFK-AS1]] (+0.70, fdr 7e-06); moves opposite to [[SLC23A2]] (-0.64, fdr 1e-05), [[MOCS1]] (-0.62, fdr 2e-05), [[ACTR5]] (-0.62, fdr 1e-05).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 2 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13147.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.27×** | +26.9 | 0e+00 | 47/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.05×** | +17.2 | 0e+00 | 43/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.30×** | +12.9 | 2e-35 | 44/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +11.2 | 7e-27 | 38/48 (A-172, SW1417, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +7.9 | 3e-13 | 33/48 (A-172, HOP62, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +6.4 | 1e-08 | 33/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.33×** | +4.4 | 8e-04 | 20/47 (CFPAC-1, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.2 | 0.002 | 19/48 (NCI-H1573, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.19× | +4.0 | 0.004 | 22/48 (LOX-IMVI, NCI-H460, …) | rises with dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.26×** | +3.8 | 0.009 | 17/48 (NCI-H1573, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.7 | 0.009 | 20/47 (SK-MEL-2, LoVo, …) | rises with dose | composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.26×** | +3.7 | 0.009 | 9/48 (PANC-1, A-172, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.6 | 0.015 | 13/48 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.081 | 8/48 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.1 | 0.082 | 15/47 (RPMI-7951, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.14× | +3.0 | 0.082 | 7/48 (SW480, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 6 with an alert ⚠. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13147.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.501×** | -11.1 | 1e-25 | 41/48 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -9.5 | 1e-18 | 37/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.581×** | -8.7 | 7e-16 | 34/47 (HT-29, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.632×** | -7.3 | 3e-11 | 30/47 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.665×** | -6.5 | 7e-09 | 28/47 (NCI-H1573, HCT15, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.696×** | -5.8 | 6e-07 | 27/48 (HT-29, SW480, …) | inconsistent across doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.688×** | -5.8 | 7e-07 | 26/46 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.768×** | -4.2 | 0.002 | 18/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.774×** | -4.1 | 0.003 | 19/48 (HT-29, NCI-H1573, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.769×** | -3.9 | 0.006 | 19/38 (Hs 766T, SHP-77, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.785×** | -3.9 | 0.006 | 15/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.639×** | -3.7 | 0.009 | 14/33 (C32, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.653×** | -3.6 | 0.016 | 16/39 (NCI-H1573, SNU-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.670×** | -3.3 | 0.033 | 13/48 (HepG2/C3A, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.760×** | -3.1 | 0.066 | 6/48 (SNU-1, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.689×** | -3.1 | 0.066 | 16/47 (J82, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Tadalafil (drug)]] 5 µM |  | **0.819×** | -3.1 | 0.072 | 16/47 (AsPC-1, SW1417, …) | top dose only |  |
| [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.05 µM |  | **0.827×** | -3.0 | 0.075 | 8/48 (Panc 03.27, HOP62, …) | inconsistent across doses |  |
| [[EX229 (drug)]] 5 µM |  | **0.700×** | -3.0 | 0.083 | 13/48 (NCI-H1573, HCT15, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Asciminib (drug)]] 0.05 µM |  | **0.830×** | -3.0 | 0.083 | 16/48 (SW48, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13147. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 73.1 | 0 | 8 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.321× (z -11.1) |
| [[SW480 (line)]] | alt | 32.9 | 3 | 5 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.68× (z +19.9) | [[Digitoxin (drug)]] 0.5 µM 0.254× (z -14.7) |
| [[NCI-H1573 (line)]] | alt | 115 | 0 | 6 (3 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.297× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.327× (z -9.9) |
| [[HCT15 (line)]] | alt | 72.1 | 0 | 5 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.213× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.277× (z -9.8) |
| [[C32 (line)]] | wt | 23.9 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.62× (z +15.2) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LoVo (line)]] | wt | 33.7 | 2 (1 ⚠) | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.47× (z +15.3) | [[Dinaciclib (drug)]] 5 µM 0.356× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[PANC-1 (line)]] | alt | 30.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +19.6) | — |
| [[SK-MEL-2 (line)]] | alt | 38.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +14.0) | [[AZD2858 (drug)]] 0.5 µM 0.161× (z -9.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 28.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.5) | — |
| [[HOP62 (line)]] | alt | 23.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +14.2) | — |
| [[NCI-H460 (line)]] | wt | 17.7 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.29× (z +15.9) | — |
| [[SHP-77 (line)]] | alt | 51.9 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0654× (z -18.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -9.0) |
| [[SNU-423 (line)]] | alt | 25.3 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.33× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.289× (z -8.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 15.0 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.47× (z +9.6) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0727× (z -10.5) |
| [[A-172 (line)]] | wt | 32.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +13.7) | — |
| [[A498 (line)]] | wt | 15.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.91× (z +18.4) | — |
| [[H4 (line)]] | wt | 15.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.35× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.105× (z -9.7) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 30.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +11.5) | [[Dinaciclib (drug)]] 0.05 µM 0.0464× (z -20.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HS-578T (line)]] | alt | 15.2 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.20× (z +14.2) | — |
| [[KATO III (line)]] | alt | 37.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +11.9) | [[Dinaciclib (drug)]] 5 µM 0.330× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change |
| [[LOX-IMVI (line)]] | wt | 17.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.34× (z +14.9) | — |
| [[LS 180 (line)]] | wt | 34.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.178× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 19.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.15× (z +13.4) | — |
| [[NCI-H23 (line)]] | alt | 35.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +12.5) | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 29.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +10.8) | — |
| [[A549 (line)]] | wt | 24.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.20× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 19.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.82× (z +12.9) | — |
| [[C-33 A (line)]] | alt | 30.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +10.0) | — |
| [[CHP-212 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Sunitinib (drug)]] 5 µM 0.0952× (z -8.7) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 25.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[hTERT-HPNE (line)]] | wt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +9.6) | — |
| [[J82 (line)]] | alt | 26.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.04× (z +11.9) | — |
| [[NCI-H1792 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.219× (z -8.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[NCI-H2030 (line)]] | alt | 21.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.97× (z +13.1) | — |
| [[NCI-H2347 (line)]] | alt | 9.50 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +10.9) | — |
| [[Panc 03.27 (line)]] | alt | 23.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +10.5) | — |
| [[RKO (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.36× (z +13.5) | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +12.6) | — |
| [[SW 900 (line)]] | alt | 19.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.25× (z +11.8) | — |
| [[A-427 (line)]] | wt | 23.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13147), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 4 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBE3B]] | +0.71 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[ARID4B]] | +0.70 | +0.58 / +0.61 | both halves | 7e-06 |  |
| [[NIFK-AS1]] | +0.70 | +0.70 / +0.59 | both halves | 7e-06 |  |
| [[CCDC30]] | +0.69 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[C2orf76]] | +0.69 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[DENND6A-AS1]] | +0.68 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | +0.67 | +0.68 / +0.45 | both halves | 3e-05 |  |
| [[MAILR]] | +0.66 | +0.71 / +0.35 | both halves | 1e-04 |  |
| [[PPP1R12A-AS2]] | +0.66 | +0.70 / +0.33 | both halves | 1e-04 |  |
| [[MZF1-AS1]] | +0.66 | +0.66 / +0.37 | both halves | 9e-05 |  |
| [[PSMD7-DT]] | +0.66 | +0.69 / +0.42 | both halves | 4e-05 |  |
| [[MED13]] | +0.66 | +0.57 / +0.39 | both halves | 6e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC23A2]] | -0.64 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[MOCS1]] | -0.62 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[ACTR5]] | -0.62 | -0.55 / -0.49 | both halves | 1e-05 |  |
| [[CS]] | -0.62 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[RSAD1]] | -0.60 | -0.55 / -0.28 | both halves | 3e-04 |  |
| [[MCOLN2]] | -0.59 | -0.55 / -0.40 | both halves | 5e-05 |  |
| [[ARRB2]] | -0.58 | -0.54 / -0.29 | both halves | 2e-04 |  |
| [[TCF3]] | -0.58 | -0.60 / -0.34 | both halves | 1e-04 |  |
| [[POLD2]] | -0.58 | -0.48 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DNASE1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.599). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (1.7, 19.2); signed map (22.6, -8.8). **Vector** length 103, 26.5% of its response variance represented; |z| ≥ 3 in 1,078 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +10.0 | +17.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +26.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +7.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.0 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.9 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.8 | -0.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | -1.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.0 | -5.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -1.9 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.2 | -1.1 |
|  | [[EX229 (drug)]] 5 µM |  | -2.6 | -3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[venetoclax (drug)]] 5 µM |  | -2.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | deoxyribonuclease 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,611,728-3,680,143 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DNL1 |
| Matched by | ensembl_id |

**Function**, from UniProt [P24855](https://www.uniprot.org/uniprotkb/P24855) (Deoxyribonuclease-1):

> Serum endocuclease secreted into body fluids by a wide variety of exocrine and endocrine organs. Expressed by non-hematopoietic tissues and preferentially cleaves protein-free DNA (By similarity). Among other functions, seems to be involved in cell death by apoptosis. Binds specifically to G-actin and blocks actin polymerization (By similarity). Together with DNASE1L3, plays a key role in degrading neutrophil extracellular traps (NETs) (By similarity). NETs are mainly composed of DNA fibers and …

**Summary**, from NCBI Gene [1773](https://www.ncbi.nlm.nih.gov/gene/1773):

> This gene encodes a member of the DNase family. This protein is stored in the zymogen granules of the nuclear envelope and functions by cleaving DNA in an endonucleolytic manner. At least six autosomal codominant alleles have been characterized, DNASE1*1 through DNASE1*6, and the sequence of DNASE1*2 represented in this record. Mutations in this gene have been associated with systemic lupus erythematosus (SLE), an autoimmune disease. A recombinant form of this protein is used to treat the one …

**Accessions** — [HGNC:2956](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2956) · Entrez [1773](https://www.ncbi.nlm.nih.gov/gene/1773) · UniProt [P24855](https://www.uniprot.org/uniprotkb/P24855) · Ensembl [ENSG00000213918](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213918)

## Data

Gene col 13147: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13147); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13147, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13147]; `tensor/DDL_lfc|DDL_z.npy` [13147]; `embed/gene_vectors.npy` [13147]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13147 or target_col == 13147). Every well: [[DNASE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNASE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
