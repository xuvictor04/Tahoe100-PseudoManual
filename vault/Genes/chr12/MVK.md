---
symbol: "MVK"
type: "gene"
col: 3180
ensembl_id: "ENSG00000110921"
name: "mevalonate kinase"
location: "12q24.11"
module: 86
arm: "+"
pooled_cpm: 8.03
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 16
n_dd_up_clean: 25
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# MVK

*mevalonate kinase* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.93× (z +19.1, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.561× (z -8.1, q 3e-13, down in 27 of 45 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MMAB]] (+0.77, fdr 7e-06, ⚠ same locus), [[SREBF2]] (+0.72, fdr 7e-06), [[MVD]] (+0.72, fdr 7e-06), [[SQLE]] (+0.71, fdr 7e-06); moves opposite to [[SPOPL-DT]] (-0.48, fdr 2e-04), [[GABPB1-AS1]] (-0.46, fdr 3e-04), [[EPM2A]] (-0.45, fdr 3e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3180.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.93×** | +19.1 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.51×** | +17.6 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **2.31×** | +16.5 | 0e+00 | 43/47 (NCI-H2030, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +15.9 | 0e+00 | 34/44 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.94×** | +13.1 | 3e-37 | 39/48 (LoVo, NCI-H2030, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.55×** | +13.1 | 3e-37 | 44/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.62×** | +6.5 | 6e-09 | 22/45 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Entrectinib (drug)]] 5 µM |  | **1.58×** | +6.4 | 1e-08 | 20/45 (NCI-H2030, HS-578T, …) | inconsistent across doses |  |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.55×** | +5.8 | 3e-07 | 16/47 (HS-578T, SNU-423, …) | top dose only | plate-row cell shift |
| [[Posaconazole (drug)]] 5 µM |  | **1.53×** | +5.7 | 8e-07 | 17/47 (HEC-1-A, A498, …) | rises with dose | plate-row cell shift |
| [[Adagrasib (drug)]] 5 µM |  | **1.51×** | +5.5 | 2e-06 | 15/47 (NCI-H2030, NCI-H460, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.31×** | +5.4 | 3e-06 | 16/47 (HEC-1-A, LoVo, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.49×** | +5.3 | 4e-06 | 10/47 (C32, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Fingolimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +4.7 | 1e-04 | 8/45 (A498, C32, …) | rises with dose |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.38×** | +4.4 | 5e-04 | 17/46 (A498, NCI-H2030, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 7e-04 | 12/47 (SW480, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3180.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.561×** | -8.1 | 3e-13 | 27/45 (HCT15, MIA PaCa-2, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.637×** | -6.1 | 3e-07 | 19/45 (NCI-H1573, CFPAC-1, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.744×** | -5.9 | 7e-07 | 19/48 (HS-578T, NCI-H2030, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.687×** | -5.3 | 2e-05 | 16/47 (NCI-H1573, CHP-212, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.698×** | -4.7 | 3e-04 | 10/23 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.730×** | -4.4 | 9e-04 | 16/45 (HS-578T, A-427, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.739×** | -4.3 | 0.002 | 15/45 (HOP62, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -4.1 | 0.003 | 16/47 (HOP62, HS-578T, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.753×** | -4.0 | 0.004 | 13/47 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.756×** | -3.9 | 0.005 | 18/47 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.760×** | -3.9 | 0.006 | 13/46 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.763×** | -3.8 | 0.006 | 17/47 (SNU-1, C32, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.763×** | -3.8 | 0.006 | 13/31 (C32, HS-578T, …) | inconsistent across doses | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.777×** | -3.6 | 0.015 | 13/47 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **0.779×** | -3.5 | 0.016 | 15/44 (LS 180, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3180. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 6.35 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.12× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.73× (z +16.4) | — |
| [[SW480 (line)]] | alt | 6.23 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.55× (z +11.2) | — |
| [[C32 (line)]] | wt | 13.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0773× (z -10.5) |
| [[HCT15 (line)]] | alt | 11.7 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0443× (z -12.4) |
| [[HOP62 (line)]] | alt | 8.94 | 1 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.36× (z +9.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.291× (z -9.3) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 12.5 | 1 | 1 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 3.38× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 7.95 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.83× (z +10.4) | — |
| [[A-427 (line)]] | wt | 10.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.156× (z -9.1) |
| [[A498 (line)]] | wt | 6.88 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.189× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[LS 180 (line)]] | wt | 7.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.29× (z +8.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 8.96 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0664× (z -11.6) |
| [[NCI-H1573 (line)]] | alt | 7.54 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0633× (z -11.8) |
| [[NCI-H23 (line)]] | alt | 7.27 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.106× (z -8.9) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.07× (z +11.1) | — |
| [[RKO (line)]] | wt | 6.26 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0781× (z -8.7) |
| [[SHP-77 (line)]] | alt | 9.39 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.143× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 7.30 | 0 | 1 | — | [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM 0.0722× (z -9.9) |
| [[SW48 (line)]] | wt | 6.07 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.25× (z +8.8) | — |
| [[A-172 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.43 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.72 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.15 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.96 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.60 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.06 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.10 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.30 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3180), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 8 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMAB]] | +0.77 | +0.81 / +0.77 | both halves | 7e-06 | STRING 778; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[SREBF2]] | +0.72 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 820 |
| [[MVD]] | +0.72 | +0.64 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 999 |
| [[SQLE]] | +0.71 | +0.67 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 859 |
| [[DHCR7]] | +0.69 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 833 |
| [[IDI1]] | +0.68 | +0.73 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 879 |
| [[HMGCR]] | +0.67 | +0.65 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 999 |
| [[FDFT1]] | +0.66 | +0.61 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 895 |
| [[INSIG1]] | +0.65 | +0.63 / +0.55 | both halves | 1e-05 | pathway: Metabolism of steroids; STRING 670 |
| [[PCYT2]] | +0.65 | +0.62 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS |
| [[ACSS2]] | +0.64 | +0.63 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 410 |
| [[ERG28]] | +0.64 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[EBP]] | +0.63 | +0.59 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 669 |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOPL-DT]] | -0.48 | -0.40 / -0.30 | both halves | 2e-04 |  |
| [[GABPB1-AS1]] | -0.46 | -0.28 / -0.33 | both halves | 3e-04 |  |
| [[EPM2A]] | -0.45 | -0.32 / -0.26 | both halves | 3e-04 |  |
| [[ARSB]] | -0.44 | -0.31 / -0.24 | both halves | 5e-04 |  |
| [[LINC01376]] | -0.43 | -0.26 / -0.25 | both halves | 4e-04 |  |
| [[WNT3]] | -0.43 | -0.19 / -0.29 | ⚠ not reproduced | 8e-04 |  |
| [[CRPPA]] | -0.42 | -0.24 / -0.28 | both halves | 5e-04 | STRING 533 |
| [[GATC]] | -0.42 | -0.34 / -0.25 | both halves | 4e-04 |  |
| [[CASC11]] | -0.42 | -0.23 / -0.32 | both halves | 5e-04 |  |
| [[ZNF124]] | -0.42 | -0.21 / -0.24 | both halves | 7e-04 |  |
| [[SUSD1]] | -0.41 | -0.23 / -0.39 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.717). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -48.6); signed map (-53.3, 31.9). **Vector** length 105, 24.6% of its response variance represented; |z| ≥ 3 in 1,182 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.51 to 19); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.55 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.53 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +6.2 | +16.5 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.6 | +13.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.3 | +15.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +19.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.0 | +17.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.8 | +6.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.4 | +3.4 |
|  | [[Posaconazole (drug)]] 5 µM |  | +3.3 | +5.7 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.1 | -8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.8 | -2.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -4.1 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -4.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | mevalonate kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,573,255-109,598,125 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LRBP, MK |
| Gene groups (HGNC) | Isoprenoid biosynthesis kinases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS |
| Reactome | 6 pathways, smallest: Lanosterol biosynthesis; Cholesterol biosynthesis; Activation of gene expression by SREBF (SREBP) |
| Matched by | ensembl_id |

**Function**, from UniProt [Q03426](https://www.uniprot.org/uniprotkb/Q03426) (Mevalonate kinase):

> Catalyzes the phosphorylation of mevalonate to mevalonate 5-phosphate, a key step in isoprenoid and cholesterol biosynthesis.

**Summary**, from NCBI Gene [4598](https://www.ncbi.nlm.nih.gov/gene/4598):

> This gene encodes the peroxisomal enzyme mevalonate kinase. Mevalonate is a key intermediate, and mevalonate kinase a key early enzyme, in isoprenoid and sterol synthesis. Mevalonate kinase deficiency caused by mutation of this gene results in mevalonic aciduria, a disease characterized psychomotor retardation, failure to thrive, hepatosplenomegaly, anemia and recurrent febrile crises. Defects in this gene also cause hyperimmunoglobulinaemia D and periodic fever syndrome, a disorder …

**Accessions** — [HGNC:7530](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7530) · Entrez [4598](https://www.ncbi.nlm.nih.gov/gene/4598) · UniProt [Q03426](https://www.uniprot.org/uniprotkb/Q03426) · Ensembl [ENSG00000110921](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110921)

## Data

Gene col 3180: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3180); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3180, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3180]; `tensor/DDL_lfc|DDL_z.npy` [3180]; `embed/gene_vectors.npy` [3180]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3180 or target_col == 3180). Every well: [[MVK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
