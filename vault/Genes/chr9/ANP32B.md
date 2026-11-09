---
symbol: "ANP32B"
type: "gene"
col: 5945
ensembl_id: "ENSG00000136938"
name: "acidic nuclear phosphoprotein 32 family member B"
location: "9q22.33"
module: 18
arm: "+"
pooled_cpm: 186.34
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# ANP32B

*acidic nuclear phosphoprotein 32 family member B* — 9q22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.62× (z +11.0, q 4e-25, up in 44 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.34× (z +3.4, q 0.054, up in 35 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A498 3.52×, A-172 3.25×, HT-29 3.28×, NCI-H1792 4.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 3.27×, HT-29 3.85×, A498 3.69×, A549 4.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 3.14×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.487× (z -12.0, q 2e-30, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX54]] (+0.62, fdr 1e-05), [[PDS5A]] (+0.58, fdr 2e-05), [[RABL6]] (+0.58, fdr 1e-05); moves opposite to [[BACH1]] (-0.55, fdr 3e-05), [[DYNLRB1]] (-0.55, fdr 2e-05), [[GALE]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SYNJ2]] → it (grade C ⚠); 1 goes from it, the strongest it → [[MZT2A]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 7 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5945.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A498 3.52×, A-172 3.25×, HT-29 3.28×, NCI-H1792 4.45×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 6 lines (KATO III 3.27×, HT-29 3.85×, A498 3.69×, A549 4.36×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 1 line (KATO III 3.14×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.62×** | +11.0 | 4e-25 | 44/44 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.04×** | +10.5 | 4e-23 | 48/49 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +7.7 | 2e-12 | 43/45 (KATO III, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | **1.90×** | +7.6 | 4e-12 | 46/48 (HT-29, Hs 766T, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.56×** | +5.0 | 5e-05 | 42/47 (HepG2/C3A, C32, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **1.38×** | +3.8 | 0.014 | 34/48 (KATO III, NCI-H460, …) | top dose only |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.4 | 0.054 | 33/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.34×** | +3.4 | 0.054 | 35/48 (NCI-H1792, C32, …) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +3.3 | 0.060 | 36/48 (HT-29, hTERT-HPNE, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.20× | +3.0 | 0.14 | 23/49 (C32, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5945.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.487×** | -12.0 | 2e-30 | 45/48 (LOX-IMVI, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.380×** | -11.4 | 8e-28 | 47/48 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.402×** | -10.8 | 9e-25 | 46/48 (J82, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.492×** | -8.4 | 9e-15 | 45/48 (KATO III, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.581×** | -6.4 | 2e-08 | 36/48 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.586×** | -6.3 | 3e-08 | 43/48 (KATO III, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.763×** | -4.5 | 6e-04 | 33/48 (KATO III, A498, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.500×** | -4.3 | 0.001 | 39/49 (J82, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.779×** | -4.2 | 0.002 | 28/48 (LS 180, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.806×** | -3.6 | 0.018 | 25/49 (MIA PaCa-2, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.738×** | -3.6 | 0.018 | 36/49 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.746×** | -3.3 | 0.042 | 31/48 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.45 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5945. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 259 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 5 µM 2.79× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -15.2) |
| [[SW480 (line)]] | alt | 239 | 2 (2 ⚠) | 5 | [[Dinaciclib (drug)]] 0.5 µM 3.52× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.8) |
| [[KATO III (line)]] | alt | 233 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.05 µM 3.14× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.243× (z -15.9) |
| [[NCI-H460 (line)]] | wt | 249 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +10.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.2) |
| [[Panc 03.27 (line)]] | alt | 177 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.0) |
| [[PANC-1 (line)]] | alt | 166 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 2.72× (z +10.5) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -12.8) |
| [[C-33 A (line)]] | alt | 226 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.9) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.285× (z -11.5) |
| [[HT-29 (line)]] | alt | 178 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.450× (z -11.0) |
| [[J82 (line)]] | alt | 290 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +9.2) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 5 µM 0.228× (z -15.7) |
| [[LOX-IMVI (line)]] | wt | 240 | 1 (1 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -21.8) |
| [[A-172 (line)]] | wt | 153 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +11.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.284× (z -12.4) |
| [[A-427 (line)]] | wt | 164 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +8.8) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.287× (z -11.7) |
| [[A498 (line)]] | wt | 249 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +12.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.327× (z -11.1) |
| [[HOP62 (line)]] | alt | 128 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.05× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -15.8) |
| [[hTERT-HPNE (line)]] | wt | 127 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.08× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.330× (z -13.1) |
| [[NCI-H2030 (line)]] | alt | 160 | 1 (1 ⚠) | 3 | [[Docetaxel (drug)]] 0.05 µM 2.29× (z +8.5) ⚠ transcription drop; cell-cycle shift, explains ~29% of this change | [[Panobinostat (drug)]] 0.5 µM 0.328× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.309× (z -14.8) |
| [[SW48 (line)]] | wt | 304 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.249× (z -12.4) |
| [[HCT15 (line)]] | alt | 198 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.3) |
| [[HS-578T (line)]] | alt | 93.4 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.38× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -9.8) |
| [[LS 180 (line)]] | wt | 203 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.298× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 80.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.63× (z +10.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.476× (z -8.5) |
| [[RKO (line)]] | wt | 261 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.354× (z -9.9) |
| [[SHP-77 (line)]] | alt | 163 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.320× (z -10.0) |
| [[SNU-1 (line)]] | wt | 254 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.9) |
| [[A549 (line)]] | wt | 232 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.70× (z +10.8) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 132 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.314× (z -10.4) |
| [[C32 (line)]] | wt | 114 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +9.4) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 183 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.279× (z -13.5) |
| [[HEC-1-A (line)]] | alt | 274 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.97× (z +9.0) ⚠ toxic; transcription drop | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -12.1) |
| [[Hs 766T (line)]] | wt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +8.5) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 191 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.04× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 128 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.45× (z +11.0) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 165 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.8) |
| [[SNU-423 (line)]] | alt | 142 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.21× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 218 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.366× (z -10.7) |
| [[AN3 CA (line)]] | alt | 211 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.280× (z -9.5) |
| [[BT-474 (line)]] | alt | 112 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.309× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 145 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.338× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 167 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.431× (z -8.8) |
| [[RPMI-7951 (line)]] | alt | 156 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.393× (z -10.8) |
| [[SW 1271 (line)]] | alt | 201 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.4) |
| [[SW 900 (line)]] | alt | 122 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 172 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 136 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 176 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 185 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 107 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5945), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX54]] | +0.62 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[PDS5A]] | +0.58 | +0.69 / +0.47 | both halves | 2e-05 |  |
| [[RABL6]] | +0.58 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PTPDC1]] | +0.57 | +0.60 / +0.42 | both halves | 4e-05 |  |
| [[ERP29]] | +0.56 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[SET]] | +0.55 | +0.45 / +0.62 | both halves | 3e-05 | STRING 462 |
| [[EIF3A]] | +0.55 | +0.32 / +0.60 | both halves | 2e-04 |  |
| [[SSRP1]] | +0.55 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[KPNB1]] | +0.53 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[UIMC1]] | +0.53 | +0.58 / +0.40 | both halves | 5e-05 |  |
| [[TMEM268]] | +0.53 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[CHPT1]] | +0.52 | +0.61 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BACH1]] | -0.55 | -0.56 / -0.44 | both halves | 3e-05 |  |
| [[DYNLRB1]] | -0.55 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[GALE]] | -0.55 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[EHD1]] | -0.55 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SFR1]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[WDR26]] | -0.53 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[BCL10]] | -0.53 | -0.57 / -0.42 | both halves | 4e-05 |  |
| [[H3-3B]] | -0.52 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[PHLDA1]] | -0.52 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[FAM43A]] | -0.52 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[SERTAD1]] | -0.51 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[HRH1]] | -0.49 | -0.45 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYNJ2]] | C | SYNJ2 activity lowers ANP32B's level | lines that do not express SYNJ2 (4) vs lines expressing it (46) | 1.39× higher at baseline in the lines without SYNJ2 | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZNF827, LINC01277, ITGA2-AS1; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MZT2A]] | C | ANP32B's natural level strengthens MZT2A's drug response | ANP32B's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.00; direction clear | 0.034 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.514). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-15.6, -49.7); signed map (-22.5, -51.4). **Vector** length 90.3, 40.2% of its response variance represented; |z| ≥ 3 in 959 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +0.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.2 | +1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +1.6 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -0.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +2.9 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.9 | +2.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.8 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.8 | -0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.6 | -12.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Vilanterol (drug)]] 0.5 µM |  | -2.6 | -0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.4 | +1.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -2.1 | +1.5 |
|  | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM |  | -2.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | acidic nuclear phosphoprotein 32 family member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q22.33 — chr9:97,983,341-98,015,943 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SSP29, PHAPI2, APRIL |
| Gene groups (HGNC) | ANP32 acidic nuclear phosphoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92688](https://www.uniprot.org/uniprotkb/Q92688) (Acidic leucine-rich nuclear phosphoprotein 32 family member B):

> Multifunctional protein that is involved in the regulation of many processes including cell proliferation, apoptosis, cell cycle progression or transcription. Regulates the proliferation of neuronal stem cells, differentiation of leukemic cells and progression from G1 to S phase of the cell cycle. As negative regulator of caspase-3-dependent apoptosis, may act as an antagonist of ANP32A in regulating tissue homeostasis. Exhibits histone chaperone properties, able to recruit histones to certain …

**Summary**, from NCBI Gene [10541](https://www.ncbi.nlm.nih.gov/gene/10541):

> Enables RNA polymerase binding activity and histone binding activity. Involved in several processes, including negative regulation of apoptotic process; nucleosome assembly; and positive regulation of protein export from nucleus. Located in cytosol; nucleolus; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16677) · Entrez [10541](https://www.ncbi.nlm.nih.gov/gene/10541) · UniProt [Q92688](https://www.uniprot.org/uniprotkb/Q92688) · Ensembl [ENSG00000136938](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136938)

## Data

Gene col 5945: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5945); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5945, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5945]; `tensor/DDL_lfc|DDL_z.npy` [5945]; `embed/gene_vectors.npy` [5945]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5945 or target_col == 5945). Every well: [[ANP32B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANP32B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
