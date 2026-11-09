---
symbol: "MRPL18"
type: "gene"
col: 3320
ensembl_id: "ENSG00000112110"
name: "mitochondrial ribosomal protein L18"
location: "6q25.3"
module: 72
arm: "+"
pooled_cpm: 24.26
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# MRPL18

*mitochondrial ribosomal protein L18* — 6q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (14 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 4.17× (z +18.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.802× (z -4.0, q 0.038, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINH1]] (+0.76, fdr 7e-06), [[BAG3]] (+0.71, fdr 7e-06), [[PSMB5]] (+0.71, fdr 7e-06); moves opposite to [[DOP1A]] (-0.57, fdr 3e-05), [[JUNB]] (-0.53, fdr 3e-05), [[SNX12]] (-0.53, fdr 4e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 14 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3320.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **4.17×** | +18.2 | 0e+00 | 48/48 (SW480, HT-29, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.49×** | +16.5 | 0e+00 | 46/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **3.10×** | +14.5 | 4e-45 | 46/47 (KATO III, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.12×** | +13.7 | 1e-40 | 48/48 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.79×** | +13.1 | 4e-37 | 46/48 (KATO III, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.41×** | +11.3 | 1e-27 | 41/41 (KATO III, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.48×** | +8.3 | 8e-15 | 42/48 (KATO III, SW1417, …) | all doses, flat | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +7.6 | 3e-12 | 39/48 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **1.87×** | +7.1 | 1e-10 | 28/42 (NCI-H460, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~28% of this change | **1.74×** | +7.1 | 1e-10 | 30/45 (HOP62, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +6.9 | 4e-10 | 31/46 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.67×** | +6.3 | 1e-08 | 32/44 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.62×** | +5.9 | 1e-07 | 34/47 (NCI-H460, C-33 A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | **1.58×** | +5.6 | 7e-07 | 23/36 (A-172, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +5.2 | 6e-06 | 29/48 (J82, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Infigratinib (drug)]] 5 µM |  | **2.03×** | +4.7 | 8e-05 | 29/47 (KATO III, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.85×** | +4.1 | 0.001 | 24/45 (KATO III, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3320.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SHP-77 0.255×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.038 | 20/48 (KATO III, SW1417, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 0.777× | -3.2 | 0.37 | 16/48 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.786× | -3.1 | 0.40 | 18/46 (AN3 CA, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.36 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3320. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 37.5 | 8 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.31× (z +20.0) | — |
| [[KATO III (line)]] | alt | 43.6 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 13.3× (z +22.1) | — |
| [[SW1417 (line)]] | alt | 28.5 | 7 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.80× (z +15.6) | — |
| [[A-172 (line)]] | wt | 22.5 | 5 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.88× (z +14.0) | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 5 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.31× (z +11.4) | — |
| [[HT-29 (line)]] | alt | 18.8 | 5 | 0 | [[Auranofin (drug)]] 5 µM 18.8× (z +17.0) | — |
| [[NCI-H460 (line)]] | wt | 18.7 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +13.9) | — |
| [[RKO (line)]] | wt | 24.4 | 5 | 0 | [[Auranofin (drug)]] 5 µM 11.1× (z +14.2) | — |
| [[A498 (line)]] | wt | 40.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 4.92× (z +13.5) | — |
| [[HS-578T (line)]] | alt | 31.1 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.08× (z +10.4) | — |
| [[J82 (line)]] | alt | 28.0 | 4 | 0 | [[Selinexor (drug)]] 5 µM 2.33× (z +9.7) | — |
| [[LoVo (line)]] | wt | 21.4 | 4 | 0 | [[Auranofin (drug)]] 5 µM 12.3× (z +16.9) | — |
| [[LS 180 (line)]] | wt | 31.4 | 4 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.59× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 22.9 | 4 | 0 | [[Auranofin (drug)]] 5 µM 11.2× (z +15.2) | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.87× (z +11.6) | — |
| [[SNU-423 (line)]] | alt | 24.1 | 4 | 0 | [[Auranofin (drug)]] 5 µM 11.7× (z +15.3) | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 3 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.87× (z +9.7) | — |
| [[C-33 A (line)]] | alt | 24.6 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.80× (z +10.4) | — |
| [[C32 (line)]] | wt | 10.8 | 2 | 0 | [[Auranofin (drug)]] 5 µM 18.3× (z +12.8) | — |
| [[HEC-1-A (line)]] | alt | 23.4 | 2 | 0 | [[Auranofin (drug)]] 5 µM 8.84× (z +16.3) | — |
| [[PANC-1 (line)]] | alt | 31.7 | 2 | 0 | [[Auranofin (drug)]] 5 µM 3.61× (z +12.7) | — |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 2 | 0 | [[Auranofin (drug)]] 5 µM 6.82× (z +11.3) | — |
| [[SW 900 (line)]] | alt | 32.3 | 2 | 0 | [[Auranofin (drug)]] 5 µM 5.34× (z +11.2) | — |
| [[A-427 (line)]] | wt | 32.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.93× (z +11.9) | — |
| [[A549 (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +11.6) | — |
| [[AsPC-1 (line)]] | alt | 18.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +11.4) | — |
| [[BT-474 (line)]] | alt | 11.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 15.5× (z +11.9) | — |
| [[HepG2_C3A (line)]] | wt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 15.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.87× (z +14.3) | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 10.7× (z +13.9) | — |
| [[NCI-H1792 (line)]] | alt | 15.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.7) | — |
| [[NCI-H2030 (line)]] | alt | 24.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.5) | — |
| [[SHP-77 (line)]] | alt | 34.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.255× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[SW48 (line)]] | wt | 24.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 8.77× (z +9.8) | — |
| [[AN3 CA (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3320), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINH1]] | +0.76 | +0.74 / +0.71 | both halves | 7e-06 | pathway: Attenuation phase |
| [[BAG3]] | +0.71 | +0.63 / +0.74 | both halves | 7e-06 | pathway: Cellular response to heat stress |
| [[PSMB5]] | +0.71 | +0.69 / +0.63 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[SOD1]] | +0.70 | +0.69 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ZFAND2A]] | +0.69 | +0.60 / +0.75 | both halves | 7e-06 |  |
| [[VIPAS39]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[PSMB4]] | +0.68 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[AHSA1]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[ALKBH6]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[HSP90AA2P]] | +0.65 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[GDAP2]] | +0.65 | +0.70 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DOP1A]] | -0.57 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[JUNB]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[SNX12]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[ZMIZ2]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[IER2]] | -0.52 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[POGZ]] | -0.52 | -0.46 / -0.51 | both halves | 2e-05 |  |
| [[PICALM]] | -0.51 | -0.43 / -0.49 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.0, -10.0); signed map (-25.1, -26.0). **Vector** length 90.4, 22.6% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Degradation of DVL* (reactome, mean cos +0.56 to 12); *proteasome* (control, mean cos +0.57 to 11); *NIK-->noncanonical NF-kB signaling* (reactome, mean cos +0.55 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +9.8 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.0 | +14.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.8 | +18.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.2 | +13.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +16.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +4.4 | +8.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +2.8 |
|  | [[Infigratinib (drug)]] 5 µM |  | +1.8 | +4.7 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -4.1 | +0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.9 | -0.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.2 | -2.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.1 | +0.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | +1.4 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.3 — chr6:159,789,812-159,798,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPC071, uL18m |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 13 pathways, smallest: Attenuation phase; HSF1 activation; HSF1-dependent transactivation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H0U6](https://www.uniprot.org/uniprotkb/Q9H0U6) (Large ribosomal subunit protein uL18m):

> Together with thiosulfate sulfurtransferase (TST), acts as a mitochondrial import factor for the cytosolic 5S rRNA. The precursor form shows RNA chaperone activity; is able to fold the 5S rRNA into an import-competent conformation that is recognized by rhodanese (TST). Both the cytoplasmic and mitochondrial forms are able to bind to the helix IV-loop D in the gamma domain of the 5S rRNA.

**Summary**, from NCBI Gene [29074](https://www.ncbi.nlm.nih.gov/gene/29074):

> This nuclear gene encodes a protein component of the larger 39S subunit of mitochondrial ribosome. This protein may also aid in the import of nuclear-encoded 5S rRNA into mitochondria. Alternative splicing results in multiple transcript variants, most of which are not predicted to encode a protein. A pseudogene of this gene is found on chromosome 16. [provided by RefSeq, Jan 2016]

**Accessions** — [HGNC:14477](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14477) · Entrez [29074](https://www.ncbi.nlm.nih.gov/gene/29074) · UniProt [Q9H0U6](https://www.uniprot.org/uniprotkb/Q9H0U6) · Ensembl [ENSG00000112110](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112110)

## Data

Gene col 3320: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3320); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3320, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3320]; `tensor/DDL_lfc|DDL_z.npy` [3320]; `embed/gene_vectors.npy` [3320]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3320 or target_col == 3320). Every well: [[MRPL18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
