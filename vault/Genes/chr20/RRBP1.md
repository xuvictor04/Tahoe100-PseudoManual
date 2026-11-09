---
symbol: "RRBP1"
type: "gene"
col: 4675
ensembl_id: "ENSG00000125844"
name: "ribosome binding protein 1"
location: "20p12.1"
module: 56
arm: "+"
pooled_cpm: 342.15
n_lines_expressing: 49
n_dd_up: 1
n_dd_down: 27
n_dd_up_clean: 1
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# RRBP1

*ribosome binding protein 1* — 20p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Auranofin (drug)]] 5 µM: 1.37× (z +5.5, q 2e-05, up in 37 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 1.95×).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -17.5, q 0e+00, down in 42 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PDXDC1]] (+0.68, fdr 7e-06), [[SEC24D]] (+0.68, fdr 7e-06), [[HM13]] (+0.68, fdr 7e-06); moves opposite to [[MTPAP]] (-0.56, fdr 1e-05), [[TBCEL]] (-0.55, fdr 2e-05), [[MCCC2]] (-0.54, fdr 4e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4675.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Auranofin (drug)]] 5 µM in 1 line (SW480 1.95×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.5 | 2e-05 | 37/47 (SW480, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4675.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.469×** | -17.5 | 0e+00 | 42/47 (NCI-H2347, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.542×** | -14.2 | 5e-43 | 46/47 (A549, C32, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.451×** | -13.3 | 3e-38 | 42/47 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.568×** | -9.9 | 1e-20 | 40/47 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.577×** | -9.2 | 4e-18 | 42/46 (C32, HOP62, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.613×** | -8.5 | 1e-15 | 36/47 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -7.4 | 1e-11 | 40/47 (H4, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.735×** | -7.2 | 5e-11 | 33/48 (HT-29, A498, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.682×** | -6.7 | 2e-09 | 34/47 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -6.6 | 2e-09 | 39/48 (HT-29, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.686×** | -6.5 | 3e-09 | 40/47 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -6.4 | 6e-09 | 38/47 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.680×** | -6.4 | 7e-09 | 41/47 (HOP62, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.704×** | -6.1 | 4e-08 | 33/47 (A498, HT-29, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.707×** | -6.0 | 6e-08 | 34/47 (KATO III, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -5.3 | 3e-06 | 33/47 (SW 900, A498, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.726×** | -5.3 | 4e-06 | 31/47 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4675. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 371 | 0 | 14 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -16.9) |
| [[A549 (line)]] | wt | 448 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -24.8) |
| [[H4 (line)]] | wt | 408 | 0 | 12 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.251× (z -15.8) |
| [[HOP62 (line)]] | alt | 600 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -16.5) |
| [[A498 (line)]] | wt | 695 | 0 | 11 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.479× (z -14.3) |
| [[HT-29 (line)]] | alt | 418 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -22.1) |
| [[HS-578T (line)]] | alt | 629 | 0 | 7 (2 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.437× (z -16.2) |
| [[KATO III (line)]] | alt | 549 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.5) |
| [[LoVo (line)]] | wt | 499 | 0 | 7 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.288× (z -16.4) |
| [[AsPC-1 (line)]] | alt | 488 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -19.6) |
| [[BT-474 (line)]] | alt | 318 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -16.0) |
| [[hTERT-HPNE (line)]] | wt | 454 | 0 | 6 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.457× (z -12.2) |
| [[SNU-1 (line)]] | wt | 299 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.265× (z -13.5) |
| [[C32 (line)]] | wt | 408 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.321× (z -17.7) |
| [[NCI-H1573 (line)]] | alt | 150 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 360 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -26.0) |
| [[RPMI-7951 (line)]] | alt | 610 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.398× (z -16.3) |
| [[A-172 (line)]] | wt | 468 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -19.2) |
| [[Hs 766T (line)]] | wt | 346 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.397× (z -15.4) |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.4) |
| [[PANC-1 (line)]] | alt | 181 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -20.2) |
| [[RKO (line)]] | wt | 421 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -13.3) |
| [[SW48 (line)]] | wt | 240 | 0 | 4 | — | [[Harringtonine (drug)]] 5 µM 0.264× (z -12.7) |
| [[NCI-H2030 (line)]] | alt | 128 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -20.8) |
| [[NCI-H23 (line)]] | alt | 161 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -19.7) |
| [[NCI-H460 (line)]] | wt | 255 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.444× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 292 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -14.6) |
| [[SNU-423 (line)]] | alt | 334 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.357× (z -16.6) |
| [[CFPAC-1 (line)]] | alt | 422 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.506× (z -12.7) |
| [[HCT15 (line)]] | alt | 414 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -16.0) |
| [[J82 (line)]] | alt | 307 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -14.3) |
| [[MIA PaCa-2 (line)]] | alt | 228 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.9) |
| [[SK-MEL-2 (line)]] | alt | 375 | 0 | 2 | — | [[Selinexor (drug)]] 5 µM 0.494× (z -13.0) |
| [[C-33 A (line)]] | alt | 190 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -9.0) |
| [[COLO 205 (line)]] | alt | 604 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[LS 180 (line)]] | wt | 381 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.552× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 152 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.481× (z -9.8) |
| [[SW480 (line)]] | alt | 181 | 1 | 0 | [[Auranofin (drug)]] 5 µM 1.95× (z +8.6) | — |
| [[A-427 (line)]] | wt | 81.2 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 191 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 130 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 250 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 504 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 336 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 310 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 133 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 532 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 328 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 236 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4675), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDXDC1]] | +0.68 | +0.72 / +0.62 | both halves | 7e-06 |  |
| [[SEC24D]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[HM13]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MANF]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[SEC13]] | +0.66 | +0.69 / +0.58 | both halves | 8e-06 |  |
| [[KDELR2]] | +0.66 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[TMED9]] | +0.66 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[ARFGAP3]] | +0.65 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[PDXDC2P]] | +0.65 | +0.69 / +0.56 | both halves | 1e-05 |  |
| [[PDXDC2P-NPIPB14P]] | +0.64 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[P4HB]] | +0.64 | +0.63 / +0.62 | both halves | 7e-06 | pathway: Dengue Virus Genome Translation and Replication |
| [[ACBD3]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTPAP]] | -0.56 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[TBCEL]] | -0.55 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[MCCC2]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MRRF]] | -0.54 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[NHLRC2]] | -0.54 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[BICRAL]] | -0.54 | -0.45 / -0.38 | both halves | 7e-05 |  |
| [[HSPBAP1]] | -0.53 | -0.55 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.691). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.7, -33.5); signed map (-52.4, 9.6). **Vector** length 132, 52.9% of its response variance represented; |z| ≥ 3 in 1,235 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.1 | +5.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.1 | -0.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | -6.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.7 | -8.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | -2.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.2 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | -2.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +0.6 |
| fall | [[Selinexor (drug)]] 5 µM |  | -13.4 | -14.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.7 | -9.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -6.0 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.7 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -5.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.0 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.9 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.7 | -2.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | -3.6 | -2.9 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ribosome binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20p12.1 — chr20:17,613,678-17,682,295 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ES/130, hES, p180 |
| Reactome | 6 pathways, smallest: Dengue Virus Genome Translation and Replication; Signaling by ALK fusions and activated point mutants; Signaling by ALK in cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P2E9](https://www.uniprot.org/uniprotkb/Q9P2E9) (Ribosome-binding protein 1):

> Acts as a ribosome receptor and mediates interaction between the ribosome and the endoplasmic reticulum membrane.

**Summary**, from NCBI Gene [6238](https://www.ncbi.nlm.nih.gov/gene/6238):

> This gene encodes a ribosome-binding protein of the endoplasmic reticulum (ER) membrane. Studies suggest that this gene plays a role in ER proliferation, secretory pathways and secretory cell differentiation, and mediation of ER-microtubule interactions. Alternative splicing has been observed and protein isoforms are characterized by regions of N-terminal decapeptide and C-terminal heptad repeats. Splicing of the tandem repeats results in variations in ribosome-binding affinity and secretory …

**Accessions** — [HGNC:10448](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10448) · Entrez [6238](https://www.ncbi.nlm.nih.gov/gene/6238) · UniProt [Q9P2E9](https://www.uniprot.org/uniprotkb/Q9P2E9) · Ensembl [ENSG00000125844](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000125844)

## Data

Gene col 4675: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4675); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4675, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4675]; `tensor/DDL_lfc|DDL_z.npy` [4675]; `embed/gene_vectors.npy` [4675]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4675 or target_col == 4675). Every well: [[RRBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RRBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
