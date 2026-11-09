---
symbol: "ZFAS1"
type: "gene"
col: 10819
ensembl_id: "ENSG00000177410"
name: "ZNFX1 antisense RNA 1"
location: "20q13.13"
module: 20
arm: "-"
pooled_cpm: 216.85
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# ZFAS1

*ZNFX1 antisense RNA 1* — 20q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (12 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.96× (z +8.5, q 1e-14, up in 46 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.108×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.488×; ⚠ cell-cycle shift, explains ~38% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 20 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GAS5]] (+0.85, fdr 7e-06), [[SNHG12]] (+0.82, fdr 7e-06), [[EPB41L4A-AS1]] (+0.80, fdr 7e-06); moves opposite to [[SRP9]] (-0.65, fdr 7e-06), [[NCBP1]] (-0.62, fdr 2e-05), [[DR1]] (-0.61, fdr 2e-05).
> It sits in the **-** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10819.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.96×** | +8.5 | 1e-14 | 46/49 (NCI-H2347, HOP62, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.96×** | +6.0 | 5e-07 | 47/48 (SK-MEL-2, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.90×** | +5.7 | 2e-06 | 38/48 (C32, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.89×** | +5.4 | 8e-06 | 43/47 (COLO 205, SHP-77, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.76×** | +4.8 | 2e-04 | 41/47 (SW 900, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.71×** | +4.8 | 2e-04 | 43/48 (SNU-1, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.70×** | +4.7 | 2e-04 | 42/48 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +4.6 | 2e-04 | 45/48 (HT-29, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +4.6 | 3e-04 | 41/50 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.67×** | +4.6 | 3e-04 | 36/49 (RKO, HCT15, …) | inconsistent across doses | composition shift |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.92×** | +4.1 | 0.002 | 47/48 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 36/48 (RPMI-7951, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.89×** | +4.0 | 0.002 | 44/48 (LoVo, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.56×** | +4.0 | 0.003 | 36/48 (NCI-H460, LoVo, …) | top dose only | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.86×** | +3.9 | 0.003 | 45/48 (AsPC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.32×** | +3.9 | 0.003 | 44/48 (SW1417, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.76×** | +3.6 | 0.009 | 38/48 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.69×** | +3.3 | 0.021 | 38/48 (LoVo, AsPC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.65×** | +3.2 | 0.033 | 32/49 (A-172, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.90×** | +3.0 | 0.060 | 31/48 (AsPC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Trametinib (drug)]] 5 µM in 1 line (NCI-H596 0.108×; ⚠ cell-cycle shift, explains ~50% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.488×; ⚠ cell-cycle shift, explains ~38% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10819. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 148 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.83× (z +16.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.22× (z +12.3) | — |
| [[AsPC-1 (line)]] | alt | 274 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.3) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.57× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 159 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.06× (z +9.5) | — |
| [[COLO 205 (line)]] | alt | 216 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.70× (z +11.2) ⚠ toxic | — |
| [[hTERT-HPNE (line)]] | wt | 138 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +8.8) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 131 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +12.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.81× (z +8.8) | — |
| [[A-172 (line)]] | wt | 146 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +9.7) | — |
| [[BT-474 (line)]] | alt | 248 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +10.7) | — |
| [[C-33 A (line)]] | alt | 368 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.5) ⚠ cell-cycle shift, explains ~38% of this change |
| [[CFPAC-1 (line)]] | alt | 218 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +9.9) | — |
| [[HEC-1-A (line)]] | alt | 123 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.22× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 125 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.52× (z +12.4) | — |
| [[Hs 766T (line)]] | wt | 292 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.27× (z +8.6) | — |
| [[J82 (line)]] | alt | 245 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +10.5) | — |
| [[KATO III (line)]] | alt | 155 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.34× (z +10.4) | — |
| [[NCI-H2347 (line)]] | alt | 178 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 264 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 4.12× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H596 (line)]] | alt | 239 | 0 | 1 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.108× (z -10.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[Panc 03.27 (line)]] | alt | 256 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +9.2) | — |
| [[SW 900 (line)]] | alt | 150 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.66× (z +9.9) | — |
| [[SW1417 (line)]] | alt | 308 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +10.4) | — |
| [[A-427 (line)]] | wt | 283 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 220 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 142 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 163 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 133 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 331 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 174 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 345 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 277 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 197 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 321 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 221 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 278 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 188 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 192 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 146 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 224 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 241 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10819), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 20 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GAS5]] | +0.85 | +0.79 / +0.89 | both halves | 7e-06 | same gene group |
| [[SNHG12]] | +0.82 | +0.77 / +0.84 | both halves | 7e-06 | same gene group |
| [[EPB41L4A-AS1]] | +0.80 | +0.79 / +0.80 | both halves | 7e-06 | same gene group |
| [[SNHG8]] | +0.78 | +0.71 / +0.82 | both halves | 7e-06 | same gene group |
| [[SNHG7]] | +0.78 | +0.78 / +0.79 | both halves | 7e-06 | same gene group |
| [[SNHG6]] | +0.75 | +0.68 / +0.79 | both halves | 7e-06 | same gene group |
| [[SNHG32]] | +0.73 | +0.66 / +0.75 | both halves | 7e-06 | same gene group |
| [[TAF1D]] | +0.72 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[RPL15]] | +0.71 | +0.55 / +0.76 | both halves | 1e-05 |  |
| [[RPL10A]] ⚠ | +0.71 | +0.61 / +0.75 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[RPS13]] ⚠ | +0.71 | +0.50 / +0.79 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RPL36A]] | +0.70 | +0.50 / +0.79 | both halves | 1e-05 |  |
| [[RPL24]] | +0.69 | +0.52 / +0.77 | both halves | 1e-05 |  |
| [[RPL31]] | +0.68 | +0.46 / +0.79 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SRP9]] | -0.65 | -0.60 / -0.66 | both halves | 7e-06 |  |
| [[NCBP1]] | -0.62 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[DR1]] | -0.61 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[TGOLN2]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[AIFM1]] | -0.58 | -0.39 / -0.56 | both halves | 5e-05 |  |
| [[POGLUT3]] | -0.57 | -0.50 / -0.62 | both halves | 1e-05 |  |
| [[CBX5]] | -0.57 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[ACTR2]] | -0.57 | -0.55 / -0.58 | both halves | 1e-05 |  |
| [[ALG10]] | -0.56 | -0.39 / -0.64 | both halves | 6e-05 |  |
| [[MAD2L1]] | -0.56 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[TARDBP]] | -0.56 | -0.31 / -0.68 | both halves | 2e-04 |  |
| [[PIGK]] | -0.56 | -0.51 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **-** arm (projection on the module's main direction -0.426). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-40.1, -28.7); signed map (-57.3, -6.0). **Vector** length 115, 49.7% of its response variance represented; |z| ≥ 3 in 1,065 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.2 | +1.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.1 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.4 | +0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +3.4 | +1.9 |
|  | [[Temsirolimus (drug)]] 5 µM |  | +3.4 | +1.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.3 | +1.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | -5.4 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.3 | -0.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.9 | +1.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.1 | +0.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.8 | -1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.6 | -1.8 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | ZNFX1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 20q13.13 — chr20:49,278,178-49,299,600 (+) |
| Ensembl biotype | lncRNA |
| Also known as | HSUP1, HSUP2; previously C20orf199, NCRNA00275, ZNFX1-AS1 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes; Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [441951](https://www.ncbi.nlm.nih.gov/gene/441951):

> This gene represents a snoRNA host gene that produces a non-coding RNA. Increased expression or amplification of this locus is associated with cancer progression and metastasis. This transcript regulates expression of genes involved in differentiation. It may act a molecular sponge for microRNAs. Alternatively spliced transcript variants have been observed. [provided by RefSeq, Dec 2017]

**Accessions** — [HGNC:33101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33101) · Entrez [441951](https://www.ncbi.nlm.nih.gov/gene/441951) · Ensembl [ENSG00000177410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177410)

## Data

Gene col 10819: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10819); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10819, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10819]; `tensor/DDL_lfc|DDL_z.npy` [10819]; `embed/gene_vectors.npy` [10819]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10819 or target_col == 10819). Every well: [[ZFAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
