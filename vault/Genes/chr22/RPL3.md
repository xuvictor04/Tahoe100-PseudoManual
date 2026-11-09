---
symbol: "RPL3"
type: "gene"
col: 1923
ensembl_id: "ENSG00000100316"
name: "ribosomal protein L3"
location: "22q13.1"
module: 20
arm: "+"
pooled_cpm: 164.79
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# RPL3

*ribosomal protein L3* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.90× (z +11.9, q 8e-30, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.52× (z +5.4, q 9e-06, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.521× (z -7.3, q 2e-10, down in 47 of 49 measured lines) ⚠ unreliable plate only; position not correctable. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0859×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (CHP-212 0.222×; ⚠ cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.223×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.350×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL4]] (+0.87, fdr 7e-06), [[RPS18]] (+0.86, fdr 7e-06), [[HNRNPA1]] (+0.79, fdr 7e-06); moves opposite to [[RBX1]] (-0.65, fdr 1e-05), [[ERVK3-1]] (-0.61, fdr 1e-05), [[ZCCHC10]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[LDHB]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.90×** | +11.9 | 8e-30 | 47/49 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +10.9 | 3e-25 | 42/44 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +7.9 | 5e-13 | 42/45 (HT-29, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.52×** | +5.4 | 9e-06 | 44/49 (C32, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.55×** | +4.9 | 9e-05 | 40/48 (SW480, KATO III, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +4.7 | 3e-04 | 41/48 (SW 900, HT-29, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~23% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.20×** | +4.6 | 3e-04 | 31/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +4.4 | 6e-04 | 37/47 (COLO 205, LoVo, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.45×** | +4.2 | 0.002 | 41/48 (SK-MEL-2, H4, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.005 | 36/48 (PANC-1, CFPAC-1, …) | two highest doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.40×** | +3.7 | 0.009 | 34/48 (SW 900, NCI-H1792, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.37×** | +3.5 | 0.020 | 30/48 (KATO III, SW480, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.34×** | +3.2 | 0.050 | 29/48 (C32, KATO III, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +3.2 | 0.050 | 21/38 (HEC-1-A, NCI-H2347, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.061 | 35/48 (NCI-H460, A549, …) | inconsistent across doses | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.69×** | +3.1 | 0.071 | 33/48 (AsPC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Malotilate (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.071 | 35/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1923.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (AN3 CA 0.0859×; ⚠ cell-cycle shift, explains ~0% of this change); [[Selinexor (drug)]] 5 µM in 1 line (CHP-212 0.222×; ⚠ cell-cycle shift, explains ~68% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.223×); [[Thymol (drug)]] 0.5 µM in 1 line (HCT15 0.350×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.521×** | -7.3 | 2e-10 | 47/49 (LS 180, AN3 CA, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.665×** | -4.5 | 0.002 | 47/49 (LS 180, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-427 (line)]] | wt | 175 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.20× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.223× (z -13.1) |
| [[HT-29 (line)]] | alt | 159 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.30× (z +11.2) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.87× (z +12.1) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 327 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.04× (z +12.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 209 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 132 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 153 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.10× (z +9.2) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 143 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.03× (z +13.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 91.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.27× (z +9.6) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 198 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.17× (z +10.1) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 148 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 189 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.84× (z +9.9) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 174 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.60× (z +10.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 132 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +10.9) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 204 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.68× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 117 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 137 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.61× (z +10.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 96.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.25× (z +9.7) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 178 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.02× (z +10.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 77.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.40× (z +9.8) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 219 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0859× (z -19.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 165 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.222× (z -14.1) ⚠ cell-cycle shift, explains ~68% of this change |
| [[COLO 205 (line)]] | alt | 65.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.19× (z +11.7) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 157 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.18× (z +8.5) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 241 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.350× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 180 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +8.6) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 168 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 188 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 160 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +9.3) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 145 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.34× (z +8.6) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 99.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.36× (z +8.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 143 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 235 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 168 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 94.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 126 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 170 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 306 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 117 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 196 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 302 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 95.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 341 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL4]] | +0.87 | +0.86 / +0.88 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS18]] | +0.86 | +0.87 / +0.85 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[HNRNPA1]] | +0.79 | +0.72 / +0.79 | both halves | 7e-06 | STRING 514 |
| [[RPL18A]] | +0.78 | +0.76 / +0.74 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1]] | +0.78 | +0.85 / +0.86 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 995 |
| [[EEF2]] | +0.77 | +0.66 / +0.80 | both halves | 7e-06 | same gene group; pathway: Eukaryotic Translation Elongation; STRING 999 |
| [[EEF1G]] | +0.76 | +0.82 / +0.68 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 968 |
| [[RPL14]] | +0.76 | +0.77 / +0.73 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPL10]] | +0.75 | +0.76 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[RPS3A]] | +0.74 | +0.77 / +0.76 | both halves | 7e-06 | same gene group; pathway: Cap-dependent Translation Initiation; STRING 999 |
| [[EEF1A1P5]] | +0.72 | +0.77 / +0.79 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[EIF4H]] | +0.70 | +0.78 / +0.70 | both halves | 7e-06 | pathway: Cap-dependent Translation Initiation; STRING 637 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RBX1]] | -0.65 | -0.56 / -0.63 | both halves | 1e-05 | pathway: Regulation of expression of SLITs and ROBOs |
| [[ERVK3-1]] | -0.61 | -0.54 / -0.62 | both halves | 1e-05 |  |
| [[ZCCHC10]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[TOPORS]] | -0.57 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[C14orf119]] | -0.56 | -0.44 / -0.60 | both halves | 3e-05 |  |
| [[DOHH]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[EID2]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[CROCCP2-1]] | -0.55 | -0.57 / -0.57 | both halves | 9e-06 |  |
| [[UNK]] | -0.55 | -0.57 / -0.44 | both halves | 3e-05 |  |
| [[MRPS18C]] | -0.53 | -0.44 / -0.60 | both halves | 3e-05 | STRING 660 |
| [[PIGBOS1]] | -0.53 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[IRX5]] | -0.53 | -0.45 / -0.50 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LDHB]] | B | LDHB activity raises RPL3's level | lines that do not express LDHB (7) vs lines expressing it (43) | 1.33× lower at baseline in the lines without LDHB | 0.089 | ⚠ within organs, on part of the lines; also absent: E2F7, ANKRD44, TMOD2; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.3, -25.5); signed map (-22.0, -34.1). **Vector** length 124, 43.6% of its response variance represented; |z| ≥ 3 in 786 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Ribosomal scanning and start codon recognition* (reactome, mean cos +0.64 to 6); *Translation initiation complex formation* (reactome, mean cos +0.64 to 6); *Activation of the mRNA upon binding of the cap-binding complex and eIFs, and subsequent binding to 43S* (reactome, mean cos +0.64 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.0 | +5.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.0 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +3.8 | +4.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +1.9 |
|  | [[Erlotinib (drug)]] 5 µM |  | +3.1 | +2.3 |
|  | [[Artesunate (drug)]] 0.05 µM |  | +3.1 | -0.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.1 | +4.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.9 | -0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.3 | +0.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.9 | -0.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.5 | -1.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.8 | -2.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -3.7 | -1.9 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -3.3 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -0.8 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -3.0 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,312,882-39,320,389 (-) |
| Ensembl biotype | protein_coding |
| Also known as | L3, uL3 |
| Gene groups (HGNC) | L ribosomal proteins; Small nucleolar RNA protein coding host genes |
| Reactome | 37 pathways, smallest: Peptide chain elongation; PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA; Viral mRNA Translation |
| Matched by | ensembl_id |

**Function**, from UniProt [P39023](https://www.uniprot.org/uniprotkb/P39023) (Large ribosomal subunit protein uL3):

> Component of the large ribosomal subunit. The ribosome is a large ribonucleoprotein complex responsible for the synthesis of proteins in the cell.

**Summary**, from NCBI Gene [6122](https://www.ncbi.nlm.nih.gov/gene/6122):

> Ribosomes, the complexes that catalyze protein synthesis, consist of a small 40S subunit and a large 60S subunit. Together these subunits are composed of 4 RNA species and approximately 80 structurally distinct proteins. This gene encodes a ribosomal protein that is a component of the 60S subunit. The protein belongs to the L3P family of ribosomal proteins and it is located in the cytoplasm. The protein can bind to the HIV-1 TAR mRNA, and it has been suggested that the protein contributes to …

**Accessions** — [HGNC:10332](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10332) · Entrez [6122](https://www.ncbi.nlm.nih.gov/gene/6122) · UniProt [P39023](https://www.uniprot.org/uniprotkb/P39023) · Ensembl [ENSG00000100316](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100316)

## Data

Gene col 1923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1923); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1923]; `tensor/DDL_lfc|DDL_z.npy` [1923]; `embed/gene_vectors.npy` [1923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1923 or target_col == 1923). Every well: [[RPL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RPL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
