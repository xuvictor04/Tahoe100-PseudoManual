---
symbol: "PMM2"
type: "gene"
col: 6440
ensembl_id: "ENSG00000140650"
name: "phosphomannomutase 2"
location: "16p13.2"
module: 52
arm: "+"
pooled_cpm: 175.08
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 29
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# PMM2

*phosphomannomutase 2* — 16p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.32× (z +7.0, q 1e-09, up in 36 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (11 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.366× (z -15.5, q 0e+00, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SEC13]] (+0.79, fdr 7e-06), [[DHDDS]] (+0.78, fdr 7e-06), [[ZNF587]] (+0.77, fdr 7e-06); moves opposite to [[KAT6A]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SEC13]] → it (grade C ⚠); 1 goes from it, the strongest it → cells under [[Lapatinib ditosylate (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6440.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.32×** | +7.0 | 1e-09 | 36/49 (COLO 205, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +6.4 | 4e-08 | 34/48 (RKO, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.48×** | +6.3 | 7e-08 | 37/48 (MIA PaCa-2, NCI-H2347, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +5.4 | 1e-05 | 0/50 | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.004 | 31/48 (LOX-IMVI, AN3 CA, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6440.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.366×** | -15.5 | 0e+00 | 46/48 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.398×** | -14.8 | 0e+00 | 46/49 (HS-578T, J82, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.532×** | -14.3 | 3e-44 | 44/48 (hTERT-HPNE, HS-578T, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.405×** | -13.9 | 5e-42 | 39/44 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.503×** | -11.0 | 4e-26 | 45/48 (A-172, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.544×** | -9.8 | 2e-20 | 43/48 (A498, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.557×** | -9.4 | 5e-19 | 45/48 (H4, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.533×** | -9.3 | 7e-19 | 40/45 (J82, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.577×** | -8.8 | 7e-17 | 39/48 (H4, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.684×** | -6.1 | 6e-08 | 38/48 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.688×** | -5.8 | 4e-07 | 36/48 (HS-578T, J82, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.777×** | -5.7 | 4e-07 | 36/48 (RPMI-7951, NCI-H460, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **0.696×** | -5.6 | 9e-07 | 32/47 (AsPC-1, A-427, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | **0.724×** | -5.2 | 9e-06 | 31/48 (LS 180, HOP62, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.726×** | -5.1 | 1e-05 | 35/48 (LoVo, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.729×** | -5.1 | 1e-05 | 36/48 (HepG2/C3A, NCI-H2030, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.564×** | -4.8 | 5e-05 | 41/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.746×** | -4.7 | 8e-05 | 31/48 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.831×** | -4.2 | 7e-04 | 24/48 (J82, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.785×** | -3.6 | 0.008 | 23/47 (A-172, A549, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.860× | -3.4 | 0.012 | 19/48 (A549, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6440. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 165 | 0 | 10 (6 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.181× (z -20.5) |
| [[HS-578T (line)]] | alt | 181 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -20.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.260× (z -15.9) |
| [[A498 (line)]] | wt | 275 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.343× (z -12.9) |
| [[H4 (line)]] | wt | 320 | 0 | 9 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.305× (z -10.5) |
| [[A549 (line)]] | wt | 224 | 0 | 8 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.227× (z -15.5) |
| [[SW1417 (line)]] | alt | 196 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -18.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.317× (z -13.4) |
| [[AsPC-1 (line)]] | alt | 490 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.436× (z -9.5) |
| [[HOP62 (line)]] | alt | 137 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -13.9) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.304× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 199 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -20.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.223× (z -14.5) |
| [[J82 (line)]] | alt | 200 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -16.6) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.449× (z -9.9) |
| [[LoVo (line)]] | wt | 226 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.316× (z -11.4) |
| [[A-427 (line)]] | wt | 113 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.4) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.303× (z -13.7) |
| [[RPMI-7951 (line)]] | alt | 194 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.235× (z -16.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.303× (z -12.8) |
| [[SW 900 (line)]] | alt | 146 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.371× (z -10.7) |
| [[KATO III (line)]] | alt | 291 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.405× (z -11.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.309× (z -10.4) |
| [[PANC-1 (line)]] | alt | 198 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.203× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.435× (z -8.8) |
| [[SW480 (line)]] | alt | 154 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.280× (z -15.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.398× (z -11.0) |
| [[HEC-1-A (line)]] | alt | 109 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.395× (z -13.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.302× (z -11.6) |
| [[Hs 766T (line)]] | wt | 222 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.196× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.431× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 156 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.302× (z -11.5) |
| [[SK-MEL-2 (line)]] | alt | 193 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0573× (z -31.8) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.437× (z -9.6) |
| [[SNU-423 (line)]] | alt | 125 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.302× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.445× (z -8.6) |
| [[C32 (line)]] | wt | 111 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.215× (z -12.8) |
| [[CFPAC-1 (line)]] | alt | 132 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.386× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HepG2_C3A (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.382× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.420× (z -8.8) |
| [[RKO (line)]] | wt | 151 | 1 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 4.29× (z +9.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.393× (z -10.7) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.437× (z -9.5) |
| [[BT-474 (line)]] | alt | 161 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change |
| [[HCT15 (line)]] | alt | 224 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -14.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 150 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.262× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1792 (line)]] | alt | 157 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.321× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 155 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0902× (z -23.0) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 90.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.8) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.383× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.332× (z -12.1) |
| [[SW 1088 (line)]] | alt | 283 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.7) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.139× (z -9.1) |
| [[SW48 (line)]] | wt | 215 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -16.3) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.190× (z -14.4) |
| [[COLO 205 (line)]] | alt | 250 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.214× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HT-29 (line)]] | alt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.375× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 112 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.321× (z -10.6) |
| [[NCI-H1573 (line)]] | alt | 204 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-1 (line)]] | wt | 180 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.341× (z -9.4) |
| [[SW 1271 (line)]] | alt | 131 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0670× (z -12.6) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 100 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 94.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 99.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6440), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC13]] | +0.79 | +0.82 / +0.82 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[DHDDS]] | +0.78 | +0.82 / +0.83 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 410 |
| [[ZNF587]] | +0.77 | +0.80 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[GOSR2]] | +0.76 | +0.68 / +0.73 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[KDELR2]] | +0.75 | +0.78 / +0.77 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[HM13]] | +0.74 | +0.78 / +0.71 | both halves | 7e-06 |  |
| [[TMED3]] | +0.74 | +0.75 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[BET1L]] | +0.73 | +0.77 / +0.70 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PGM3]] | +0.72 | +0.68 / +0.68 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 592 |
| [[PDIA5]] | +0.71 | +0.79 / +0.66 | both halves | 7e-06 |  |
| [[NDEL1]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[SEC61A1]] | +0.71 | +0.75 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KAT6A]] | -0.62 | -0.50 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC13]] | C | SEC13's natural level strengthens PMM2's drug response | SEC13's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.26; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PDXDC1]] | C | PDXDC1's natural level strengthens PMM2's drug response | PDXDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.33; direction not clear | 0.040 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Lapatinib ditosylate (drug)]] 0.5 µM | C | PMM2's natural level raises the cells' numbers under Lapatinib ditosylate 0.5 µM (protects the cells) | PMM2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63 | 0.406 over the table, 0.059 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.814). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (11.3, -29.4); signed map (-49.7, 7.3). **Vector** length 134, 54.8% of its response variance represented; |z| ≥ 3 in 1,362 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.4 | +4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.9 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | +7.3 | -4.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.8 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.7 | +2.2 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.5 | +2.7 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.7 | -15.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -6.8 | -11.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | -5.9 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -5.5 | -14.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -4.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.1 | -5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.8 | -3.4 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.7 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | phosphomannomutase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.2 — chr16:8,788,823-8,862,534 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDGS, CDG1a, PMI, PMI1; previously CDG1 |
| Gene groups (HGNC) | HAD Asp-based non-protein phosphatases |
| Hallmark sets | GLYCOLYSIS |
| Reactome | 7 pathways, smallest: Synthesis of GDP-mannose; Diseases associated with glycosylation precursor biosynthesis; Synthesis of substrates in N-glycan biosythesis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15305](https://www.uniprot.org/uniprotkb/O15305) (Phosphomannomutase 2):

> Involved in the synthesis of the GDP-mannose and dolichol-phosphate-mannose required for a number of critical mannosyl transfer reactions.

**Summary**, from NCBI Gene [5373](https://www.ncbi.nlm.nih.gov/gene/5373):

> The protein encoded by this gene catalyzes the isomerization of mannose 6-phosphate to mannose 1-phosphate, which is a precursor to GDP-mannose necessary for the synthesis of dolichol-P-oligosaccharides. Mutations in this gene have been shown to cause defects in glycoprotein biosynthesis, which manifests as carbohydrate-deficient glycoprotein syndrome type I. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9115) · Entrez [5373](https://www.ncbi.nlm.nih.gov/gene/5373) · UniProt [O15305](https://www.uniprot.org/uniprotkb/O15305) · Ensembl [ENSG00000140650](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000140650)

## Data

Gene col 6440: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6440); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6440, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6440]; `tensor/DDL_lfc|DDL_z.npy` [6440]; `embed/gene_vectors.npy` [6440]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6440 or target_col == 6440). Every well: [[PMM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
