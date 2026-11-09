---
symbol: "CBX3"
type: "gene"
col: 4352
ensembl_id: "ENSG00000122565"
name: "chromobox 3"
location: "7p15.2"
module: 67
arm: "+"
pooled_cpm: 222.77
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 3
n_dd_up_clean: 0
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/067"]
generated_by: "tahoemap"
---

# CBX3

*chromobox 3* — 7p15.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.56× (z +13.8, q 1e-40, up in 49 of 49 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1792 9.81×, A549 7.22×, HT-29 5.22×, NCI-H460 5.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 6.39×, NCI-H1792 7.48×, HT-29 3.95×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.471× (z -11.5, q 5e-28, down in 46 of 48 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THSD4-AS1]] (+0.67, fdr 2e-05), [[MIS18BP1]] (+0.62, fdr 7e-06), [[PARPBP]] (+0.59, fdr 3e-05); moves opposite to [[OTUB1]] (-0.57, fdr 3e-05), [[STXBP2]] (-0.56, fdr 9e-05), [[AMZ2P1-1]] (-0.55, fdr 1e-04).
> It is in [[Module 067]], a single-armed module (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AURKB]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4352.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 12 lines (NCI-H1792 9.81×, A549 7.22×, HT-29 5.22×, NCI-H460 5.13×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (A549 6.39×, NCI-H1792 7.48×, HT-29 3.95×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.56×** | +13.8 | 1e-40 | 49/49 (NCI-H1792, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.86×** | +11.0 | 1e-25 | 44/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.38×** | +8.7 | 5e-16 | 43/45 (SNU-423, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~47% of this change | **1.72×** | +5.9 | 5e-07 | 47/48 (HT-29, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.49×** | +4.2 | 0.003 | 37/47 (C32, H4, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.28×** | +3.9 | 0.010 | 44/48 (SW48, NCI-H2030, …) | top dose only |  |
| [[Bendamustine (drug)]] 5 µM |  | 1.34× | +3.1 | 0.16 | 32/48 (AsPC-1, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4352.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.471×** | -11.5 | 5e-28 | 46/48 (BT-474, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.621×** | -5.2 | 7e-05 | 40/48 (AN3 CA, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.666×** | -4.4 | 0.002 | 40/48 (A-427, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.559× | -3.3 | 0.14 | 30/49 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.744× | -3.2 | 0.16 | 34/48 (A-427, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.54 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4352. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 373 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.15× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -10.9) |
| [[HOP62 (line)]] | alt | 159 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -8.5) |
| [[HT-29 (line)]] | alt | 245 | 4 (4 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +16.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -11.8) |
| [[KATO III (line)]] | alt | 289 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.422× (z -11.3) |
| [[MIA PaCa-2 (line)]] | alt | 251 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 4.30× (z +13.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.287× (z -15.8) |
| [[HS-578T (line)]] | alt | 179 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.51× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -11.1) |
| [[SW480 (line)]] | alt | 312 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.92× (z +12.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.343× (z -13.3) |
| [[A549 (line)]] | wt | 161 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.22× (z +16.6) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 145 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +12.4) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 115 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.36× (z +12.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 122 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.09× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.421× (z -9.6) |
| [[hTERT-HPNE (line)]] | wt | 144 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -11.3) |
| [[J82 (line)]] | alt | 219 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.37× (z +11.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.4) |
| [[LoVo (line)]] | wt | 211 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.3) |
| [[NCI-H1792 (line)]] | alt | 86.9 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 9.81× (z +17.2) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 178 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +12.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2347 (line)]] | alt | 233 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.502× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 176 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +14.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 215 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.15× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -12.4) |
| [[RKO (line)]] | wt | 180 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.58× (z +11.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -14.6) |
| [[SNU-423 (line)]] | alt | 181 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.78× (z +14.4) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 190 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.93× (z +10.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.413× (z -11.8) |
| [[SW1417 (line)]] | alt | 272 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +12.7) ⚠ toxic; transcription drop | — |
| [[SW48 (line)]] | wt | 317 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -10.5) |
| [[A-172 (line)]] | wt | 260 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.86× (z +13.3) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 317 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -13.7) |
| [[CHP-212 (line)]] | wt | 246 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.4) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 137 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -15.3) |
| [[H4 (line)]] | wt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +10.9) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 242 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.416× (z -9.5) |
| [[Hs 766T (line)]] | wt | 174 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.82× (z +12.4) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 212 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +10.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -11.0) |
| [[NCI-H1573 (line)]] | alt | 97.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.37× (z +13.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.492× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 267 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.56× (z +12.5) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 291 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.95× (z +13.7) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 250 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +11.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -12.7) |
| [[SK-MEL-2 (line)]] | alt | 297 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -11.0) |
| [[SNU-1 (line)]] | wt | 180 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.61× (z +9.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.287× (z -9.8) |
| [[A-427 (line)]] | wt | 280 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.59× (z +8.6) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.465× (z -10.5) |
| [[BT-474 (line)]] | alt | 238 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.57× (z +10.9) ⚠ toxic; transcription drop | — |
| [[SW 1271 (line)]] | alt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.258× (z -10.6) |
| [[C-33 A (line)]] | alt | 240 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 314 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 162 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 266 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 254 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4352), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 3 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THSD4-AS1]] | +0.67 | +0.75 / +0.46 | both halves | 2e-05 |  |
| [[MIS18BP1]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[PARPBP]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[LMNB1]] | +0.58 | +0.67 / +0.42 | both halves | 4e-05 | STRING 480 |
| [[KIF18B]] | +0.58 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[BUB1B]] | +0.57 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[HMGB1]] | +0.57 | +0.54 / +0.68 | both halves | 1e-05 | STRING 512 |
| [[CEP55]] | +0.57 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GMPS]] | +0.57 | +0.72 / +0.31 | both halves | 2e-04 |  |
| [[CEP85]] | +0.56 | +0.59 / +0.37 | both halves | 8e-05 |  |
| [[PBK]] | +0.56 | +0.62 / +0.37 | both halves | 7e-05 |  |
| [[OIP5]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[OTUB1]] | -0.57 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[STXBP2]] | -0.56 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[AMZ2P1-1]] | -0.55 | -0.63 / -0.34 | both halves | 1e-04 |  |
| [[DXO]] | -0.53 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[MUL1]] | -0.53 | -0.56 / -0.31 | both halves | 2e-04 |  |
| [[LAMTOR1]] | -0.52 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[ZSWIM1]] | -0.52 | -0.64 / -0.27 | both halves | 3e-04 |  |
| [[MYL5]] | -0.52 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[PI4KB]] | -0.51 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[TRIP6]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[TNK1]] | -0.50 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[FASTK]] | -0.50 | -0.39 / -0.47 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AURKB]] | C | AURKB activity raises CBX3's level | lines that do not express AURKB (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without AURKB | 0.042 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: TCF19, SMARCD3, CDC45; maybe low, not absent |
| [[PBK]] | C | PBK activity raises CBX3's level | lines that do not express PBK (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without PBK | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPDL1, SMARCD3, NCS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 067]] — E2F targets; 73 genes; every member is in the + arm (projection on the module's main direction 0.588). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-34.1, -54.5); signed map (-47.1, -40.4). **Vector** length 67.7, 27.1% of its response variance represented; |z| ≥ 3 in 754 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Deposition of new CENPA-containing nucleosomes at the centromere* (reactome, mean cos +0.52 to 4); *Nucleosome assembly* (reactome, mean cos +0.52 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | -0.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.5 | -0.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +2.3 | +4.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | -1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -1.4 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.5 µM |  | +1.5 | +0.3 |
|  | [[Adenosine (drug)]] 0.5 µM |  | +1.3 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.3 | +2.4 |
|  | [[Belinostat (drug)]] 0.05 µM |  | +1.2 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.5 | -5.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.2 | -11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.9 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.5 | +13.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -3.6 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.2 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.8 | +1.8 |

## What is on record

|  |  |
|---|---|
| Name | chromobox 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p15.2 — chr7:26,201,162-26,213,607 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HP1Hs-gamma, HP1gamma |
| Gene groups (HGNC) | Chromobox family |
| Hallmark sets | MYC_TARGETS_V2, MYC_TARGETS_V1 |
| Reactome | 11 pathways, smallest: ChAHP complex assembly; ERCC6 (CSB) and EHMT2 (G9a) positively regulate rRNA expression; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13185](https://www.uniprot.org/uniprotkb/Q13185) (Chromobox protein homolog 3):

> Component of heterochromatin, which recognizes and binds histone H3 tails methylated at 'Lys-9', leading to epigenetic repression. Also recognizes and binds histone H1.4 methylated at 'Lys-26' (H1.4K26me). Excluded from chromatin when histone H1.4 is Simultaneously methylated at Lys-26 (H1.4K26me) and phosphorylated at Ser-27 (H1.4S27Ph). Involved in the formation of functional kinetochore through interaction with MIS12 complex proteins. Contributes to the conversion of local chromatin to a …

**Summary**, from NCBI Gene [11335](https://www.ncbi.nlm.nih.gov/gene/11335):

> At the nuclear envelope, the nuclear lamina and heterochromatin are adjacent to the inner nuclear membrane. The protein encoded by this gene binds DNA and is a component of heterochromatin. This protein also can bind lamin B receptor, an integral membrane protein found in the inner nuclear membrane. The dual binding functions of the encoded protein may explain the association of heterochromatin with the inner nuclear membrane. This protein binds histone H3 tails methylated at Lys-9 sites. This …

**Accessions** — [HGNC:1553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1553) · Entrez [11335](https://www.ncbi.nlm.nih.gov/gene/11335) · UniProt [Q13185](https://www.uniprot.org/uniprotkb/Q13185) · Ensembl [ENSG00000122565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122565)

## Data

Gene col 4352: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4352); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4352, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4352]; `tensor/DDL_lfc|DDL_z.npy` [4352]; `embed/gene_vectors.npy` [4352]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4352 or target_col == 4352). Every well: [[CBX3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CBX3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
