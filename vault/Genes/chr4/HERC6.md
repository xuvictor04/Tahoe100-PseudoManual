---
symbol: "HERC6"
type: "gene"
col: 6202
ensembl_id: "ENSG00000138642"
name: "HECT and RLD domain containing E3 ubiquitin protein ligase family member 6"
location: "4q22.1"
module: 32
arm: "+"
pooled_cpm: 40.66
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 49
n_dd_up_clean: 22
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 78
direction_downstream: 69
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# HERC6

*HECT and RLD domain containing E3 ubiquitin protein ligase family member 6* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 1.81× (z +5.7, q 5e-06, up in 29 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 49 drug-doses (13 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.186× (z -16.3, q 0e+00, down in 41 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP9]] (+0.92, fdr 7e-06), [[CMPK2]] (+0.92, fdr 7e-06), [[PARP14]] (+0.91, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 78 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 69 go from it, the strongest it → [[NLRC5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6202.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **1.81×** | +5.7 | 5e-06 | 29/43 (NCI-H2347, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.66×** | +4.7 | 4e-04 | 30/42 (Hs 766T, KATO III, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.42×** | +4.7 | 4e-04 | 29/43 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.39×** | +3.8 | 0.014 | 24/43 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.35×** | +3.8 | 0.014 | 22/43 (Hs 766T, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 0.05 µM |  | **1.51×** | +3.8 | 0.014 | 21/43 (LS 180, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.46×** | +3.8 | 0.014 | 23/44 (Hs 766T, NCI-H1792, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.014 | 25/42 (Hs 766T, LoVo, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.014 | 21/43 (NCI-H2347, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.015 | 25/43 (Panc 03.27, NCI-H2347, …) | rises with dose |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.44×** | +3.5 | 0.021 | 19/43 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.024 | 21/43 (Hs 766T, LoVo, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.030 | 16/43 (NCI-H460, C32, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.040 | 19/43 (Hs 766T, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.040 | 22/43 (NCI-H2030, CHP-212, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.40×** | +3.2 | 0.043 | 15/42 (NCI-H1792, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 13 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 49 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6202.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.186×** | -16.3 | 0e+00 | 41/43 (NCI-H1792, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.224×** | -14.5 | 4e-45 | 40/42 (SNU-423, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.225×** | -14.4 | 6e-45 | 41/43 (CFPAC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.235×** | -14.0 | 2e-42 | 42/43 (NCI-H1792, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.380×** | -13.3 | 5e-38 | 31/43 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.280×** | -12.3 | 7e-33 | 37/43 (LoVo, BT-474, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.302×** | -11.6 | 4e-29 | 36/43 (MIA PaCa-2, SNU-423, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.437×** | -11.3 | 6e-28 | 32/44 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.348×** | -10.2 | 1e-22 | 37/43 (NCI-H1792, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.428×** | -8.2 | 1e-14 | 31/43 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.222×** | -7.6 | 1e-12 | 36/43 (RPMI-7951, NCI-H1792, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.457×** | -7.6 | 2e-12 | 31/43 (BT-474, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.454×** | -7.4 | 8e-12 | 26/42 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **0.488×** | -6.9 | 2e-10 | 28/41 (RKO, SNU-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.515×** | -6.4 | 5e-09 | 31/43 (SNU-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.516×** | -6.4 | 6e-09 | 27/43 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.629×** | -6.3 | 8e-09 | 26/43 (SNU-423, BT-474, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6202. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 94.4 | 0 | 23 (8 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0524× (z -18.3) |
| [[BT-474 (line)]] | alt | 73.3 | 0 | 16 (4 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0475× (z -18.0) |
| [[LoVo (line)]] | wt | 111 | 0 | 16 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0426× (z -19.9) |
| [[MIA PaCa-2 (line)]] | alt | 74.4 | 0 | 16 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0231× (z -20.8) |
| [[AsPC-1 (line)]] | alt | 52.5 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0412× (z -16.7) |
| [[NCI-H1792 (line)]] | alt | 84.2 | 0 | 14 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0261× (z -23.0) |
| [[SNU-423 (line)]] | alt | 43.5 | 0 | 13 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0441× (z -19.3) |
| [[RPMI-7951 (line)]] | alt | 110 | 0 | 12 | — | [[Panobinostat (drug)]] 0.05 µM 0.0764× (z -16.8) |
| [[NCI-H2347 (line)]] | alt | 58.2 | 4 (1 ⚠) | 6 | [[Homoharringtonine (drug)]] 0.5 µM 4.57× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.191× (z -12.1) |
| [[A-172 (line)]] | wt | 92.3 | 0 | 9 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0139× (z -22.2) |
| [[A549 (line)]] | wt | 36.1 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.7) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.290× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 55.5 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0784× (z -18.5) |
| [[SNU-1 (line)]] | wt | 48.6 | 0 | 9 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0330× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0505× (z -11.3) |
| [[HS-578T (line)]] | alt | 32.0 | 0 | 8 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0494× (z -15.2) |
| [[KATO III (line)]] | alt | 65.9 | 0 | 8 | — | [[Belinostat (drug)]] 5 µM 0.0254× (z -19.6) |
| [[COLO 205 (line)]] | alt | 72.5 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0547× (z -14.1) |
| [[NCI-H460 (line)]] | wt | 31.5 | 3 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 3.87× (z +15.9) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 3.84× (z +10.7) | [[Belinostat (drug)]] 5 µM 0.165× (z -15.0) |
| [[Panc 03.27 (line)]] | alt | 66.2 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.0952× (z -14.7) |
| [[Hs 766T (line)]] | wt | 76.5 | 0 | 5 | — | [[Panobinostat (drug)]] 0.5 µM 0.0600× (z -16.3) |
| [[LS 180 (line)]] | wt | 47.5 | 1 (1 ⚠) | 4 | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +10.1) ⚠ cell-cycle shift, explains ~54% of this change | [[Belinostat (drug)]] 5 µM 0.149× (z -13.4) |
| [[NCI-H1573 (line)]] | alt | 39.6 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -13.5) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.223× (z -11.2) |
| [[J82 (line)]] | alt | 38.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 5.88× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.213× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 35.3 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0735× (z -13.9) |
| [[SHP-77 (line)]] | alt | 22.2 | 0 | 4 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.122× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 40.5 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.205× (z -8.9) |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -10.9) |
| [[CHP-212 (line)]] | wt | 42.9 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0684× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 10.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.4) ⚠ cell-cycle shift, explains ~54% of this change | [[Cobimetinib (drug)]] 0.05 µM 0.198× (z -8.6) |
| [[A498 (line)]] | wt | 39.7 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.184× (z -9.1) |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0246× (z -16.0) |
| [[C32 (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.20× (z +8.6) ⚠ cell-cycle shift, explains ~54% of this change | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.168× (z -8.6) |
| [[SW 900 (line)]] | alt | 29.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -9.7) |
| [[SW48 (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[Nimesulide (drug)]] 5 µM 0.0894× (z -8.9) ⚠ toxic; unreliable plate only |
| [[A-427 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.67 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.85 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.95 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.15 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6202), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP9]] | +0.92 | +0.89 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 663 |
| [[CMPK2]] | +0.92 | +0.90 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 685 |
| [[PARP14]] | +0.91 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 569 |
| [[DDX60L]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | STRING 466 |
| [[RSAD2]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 903 |
| [[MX1]] | +0.91 | +0.89 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 887 |
| [[IFIT3]] | +0.90 | +0.89 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 879 |
| [[OAS2]] | +0.90 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 893 |
| [[IFIT1]] | +0.90 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 882 |
| [[XAF1]] | +0.90 | +0.83 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 864 |
| [[USP18]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 902 |
| [[IFI44]] | +0.90 | +0.88 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 908 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*78 arrows, 78 of them with an alert ⚠; grade A 0, B 50, C 28. Shown: the 12 strongest; 66 more arrows (66 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises HERC6's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.02× lower at baseline in the lines without OAS2 | 7e-05 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[TRIM22]] | B | TRIM22 activity raises HERC6's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without TRIM22 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CMPK2]] | B | CMPK2 activity raises HERC6's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.10× lower at baseline in the lines without CMPK2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[OAS2]] | B | OAS2 activity strengthens HERC6's drug response | lines that do not express OAS2 (9) vs lines expressing it (35) | the lines without OAS2 respond 0.40× as strongly (z diff +3.02); strongest at Panobinostat 5 µM: 0.38x vs 0.14x (z diff +3.7) | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[OAS1]] | B | OAS1 activity raises HERC6's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.06× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises HERC6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.43× lower at baseline in the lines without SAMD9L | 7e-04 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[MX1]] | B | MX1 activity raises HERC6's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.37× lower at baseline in the lines without MX1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[RSAD2]] | B | RSAD2 activity raises HERC6's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without RSAD2 | 0.001 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[NRIR]] | B | NRIR activity raises HERC6's level | lines that do not express NRIR (14) vs lines expressing it (36) | 2.43× lower at baseline in the lines without NRIR | 0.001 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[PLSCR1]] | B | PLSCR1 activity raises HERC6's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.97× lower at baseline in the lines without PLSCR1 | 0.002 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[IFITM1]] | B | IFITM1 activity raises HERC6's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without IFITM1 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI44]] | B | IFI44 activity raises HERC6's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.50× lower at baseline in the lines without IFI44 | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 55, C 14. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NLRC5]] | B | HERC6 activity raises NLRC5's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.20× lower at baseline in the lines without HERC6 | 0.003 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SP110]] | B | HERC6 activity raises SP110's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.72× lower at baseline in the lines without HERC6 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[IFI44]] | B | HERC6 activity raises IFI44's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 5.04× lower at baseline in the lines without HERC6 | 0.007 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[RSAD2]] | B | HERC6 activity raises RSAD2's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 5.55× lower at baseline in the lines without HERC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[OAS1]] | B | HERC6 activity raises OAS1's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 4.88× lower at baseline in the lines without HERC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[TRANK1]] | B | HERC6 activity raises TRANK1's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.94× lower at baseline in the lines without HERC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[DDX60]] | B | HERC6 activity raises DDX60's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.06× lower at baseline in the lines without HERC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[PLSCR1]] | B | HERC6 activity raises PLSCR1's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.92× lower at baseline in the lines without HERC6 | 0.010 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SAMD9]] | B | HERC6 activity raises SAMD9's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 4.65× lower at baseline in the lines without HERC6 | 0.012 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[OAS3]] | B | HERC6 activity raises OAS3's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 3.98× lower at baseline in the lines without HERC6 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[APOL6]] | B | HERC6 activity raises APOL6's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.65× lower at baseline in the lines without HERC6 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SP100]] | B | HERC6 activity raises SP100's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 2.66× lower at baseline in the lines without HERC6 | 0.013 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.925). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.0, 54.0); signed map (64.3, 32.0). **Vector** length 148, 55.2% of its response variance represented; |z| ≥ 3 in 1,597 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.85 to 23); *Interferon Signaling* (reactome, mean cos +0.79 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.82 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +12.2 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +11.8 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +9.8 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | +7.9 | -5.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.5 | +3.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.8 | +3.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.9 | +4.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +4.3 | +1.8 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.1 | +3.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.6 | -13.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.8 | -11.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.2 | -8.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.1 | -7.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.7 | -11.6 |

## What is on record

|  |  |
|---|---|
| Name | HECT and RLD domain containing E3 ubiquitin protein ligase family member 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,378,739-88,443,097 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20637 |
| Gene groups (HGNC) | HECT and RLD domain containing E3 ubiquitin protein ligases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Antigen processing: Ubiquitination & Proteasome degradation; Class I MHC mediated antigen processing & presentation; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IVU3](https://www.uniprot.org/uniprotkb/Q8IVU3) (Probable E3 ISG15--protein ligase HERC6):

> Major E3 ligase for ISG15 conjugation. Acts as a positive regulator of innate antiviral response in cells induced by interferon.

**Summary**, from NCBI Gene [55008](https://www.ncbi.nlm.nih.gov/gene/55008):

> HERC6 belongs to the HERC family of ubiquitin ligases, all of which contain a HECT domain and at least 1 RCC1 (MIM 179710)-like domain (RLD). The 350-amino acid HECT domain is predicted to catalyze the formation of a thioester with ubiquitin before transferring it to a substrate, and the RLD is predicted to act as a guanine nucleotide exchange factor for small G proteins (Hochrainer et al., 2005 [PubMed 15676274]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:26072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26072) · Entrez [55008](https://www.ncbi.nlm.nih.gov/gene/55008) · UniProt [Q8IVU3](https://www.uniprot.org/uniprotkb/Q8IVU3) · Ensembl [ENSG00000138642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138642)

## Data

Gene col 6202: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6202); `tables/drug_effects.parquet` (72 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6202, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6202]; `tensor/DDL_lfc|DDL_z.npy` [6202]; `embed/gene_vectors.npy` [6202]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6202 or target_col == 6202). Every well: [[HERC6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HERC6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
