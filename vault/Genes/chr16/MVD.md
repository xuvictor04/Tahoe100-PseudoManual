---
symbol: "MVD"
type: "gene"
col: 9473
ensembl_id: "ENSG00000167508"
name: "mevalonate diphosphate decarboxylase"
location: "16q24.2"
module: 86
arm: "+"
pooled_cpm: 19.96
n_lines_expressing: 50
n_dd_up: 23
n_dd_down: 14
n_dd_up_clean: 20
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# MVD

*mevalonate diphosphate decarboxylase* — 16q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (3 with an alert ⚠); the strongest is [[Cepharanthine (drug)]] 5 µM: 2.47× (z +12.6, q 2e-33, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.525× (z -6.1, q 5e-07, down in 31 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FDPS]] (+0.87, fdr 7e-06), [[ACSS2]] (+0.85, fdr 7e-06), [[SREBF2]] (+0.85, fdr 7e-06); moves opposite to [[ZNF462]] (-0.57, fdr 2e-05), [[TRMT5]] (-0.57, fdr 2e-05), [[TFAM]] (-0.56, fdr 2e-05).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9473.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cepharanthine (drug)]] 5 µM |  | **2.47×** | +12.6 | 2e-33 | 46/48 (LS 180, HOP62, …) | top dose only |  |
| [[Berbamine (drug)]] 5 µM |  | **2.37×** | +12.0 | 1e-30 | 46/48 (LS 180, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +8.5 | 5e-15 | 42/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.00×** | +6.8 | 1e-09 | 39/47 (RKO, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.95×** | +6.2 | 7e-08 | 34/46 (MIA PaCa-2, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.81×** | +5.6 | 2e-06 | 28/41 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +5.4 | 5e-06 | 28/47 (RKO, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +5.2 | 2e-05 | 30/47 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.68×** | +4.9 | 7e-05 | 28/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.61×** | +4.6 | 2e-04 | 26/47 (HS-578T, NCI-H2030, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.92×** | +4.6 | 2e-04 | 28/48 (MIA PaCa-2, LS 180, …) | all doses, flat | noisy plate (z scaled) |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.59×** | +4.4 | 5e-04 | 28/48 (C32, HS-578T, …) | top dose only | plate-row cell shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 26/47 (C32, NCI-H2030, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.34×** | +4.0 | 0.002 | 18/48 (LS 180, PANC-1, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.12×** | +3.9 | 0.004 | 20/39 (MIA PaCa-2, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Terfenadine (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.004 | 23/48 (NCI-H2030, LS 180, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.47×** | +3.6 | 0.009 | 20/47 (HOP62, C-33 A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9473.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.525×** | -6.1 | 5e-07 | 31/46 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.649×** | -6.0 | 5e-07 | 34/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.568×** | -5.6 | 4e-06 | 32/47 (HS-578T, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.354×** | -5.3 | 1e-05 | 30/48 (A-427, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.583×** | -5.1 | 4e-05 | 29/46 (LS 180, KATO III, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.413×** | -4.5 | 5e-04 | 26/44 (PANC-1, HS-578T, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.660×** | -4.1 | 0.003 | 21/47 (SW48, KATO III, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.663×** | -4.0 | 0.004 | 24/47 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.683×** | -3.6 | 0.024 | 23/47 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -3.3 | 0.048 | 18/48 (A498, RPMI-7951, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.704×** | -3.2 | 0.070 | 22/44 (HS-578T, SW48, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **0.727×** | -3.2 | 0.072 | 16/48 (NCI-H1792, NCI-H1573, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -3.1 | 0.072 | 6/48 (NCI-H1573, HOP62, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.730×** | -3.1 | 0.076 | 16/48 (NCI-H2030, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.03 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9473. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 72.9 | 1 | 3 (1 ⚠) | [[Cepharanthine (drug)]] 5 µM 2.90× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.201× (z -8.9) |
| [[HS-578T (line)]] | alt | 28.0 | 2 | 1 | [[Berbamine (drug)]] 5 µM 4.42× (z +12.3) | [[Harringtonine (drug)]] 0.5 µM 0.220× (z -8.8) |
| [[A498 (line)]] | wt | 28.3 | 1 | 1 | [[Berbamine (drug)]] 5 µM 2.64× (z +10.0) | [[Selinexor (drug)]] 5 µM 0.435× (z -8.6) |
| [[A549 (line)]] | wt | 12.3 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.08× (z +10.0) | — |
| [[C-33 A (line)]] | alt | 18.3 | 2 | 0 | [[Berbamine (drug)]] 5 µM 5.64× (z +10.8) | — |
| [[C32 (line)]] | wt | 9.76 | 2 | 0 | [[Berbamine (drug)]] 5 µM 5.81× (z +8.8) | — |
| [[HEC-1-A (line)]] | alt | 15.8 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.06× (z +10.7) | — |
| [[HOP62 (line)]] | alt | 13.4 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 4.02× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 21.8 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 3.93× (z +11.5) | — |
| [[KATO III (line)]] | alt | 37.5 | 1 | 1 | [[Cepharanthine (drug)]] 5 µM 3.12× (z +9.4) | [[Homoharringtonine (drug)]] 0.5 µM 0.153× (z -10.9) |
| [[LoVo (line)]] | wt | 14.2 | 2 | 0 | [[Berbamine (drug)]] 5 µM 4.76× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 29.6 | 2 | 0 | [[Berbamine (drug)]] 5 µM 5.61× (z +13.6) | — |
| [[NCI-H2030 (line)]] | alt | 32.7 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 5.15× (z +12.2) | — |
| [[NCI-H23 (line)]] | alt | 8.44 | 2 | 0 | [[Cepharanthine (drug)]] 5 µM 6.05× (z +10.6) | — |
| [[A-427 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -10.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HCT15 (line)]] | alt | 27.8 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0834× (z -11.9) |
| [[hTERT-HPNE (line)]] | wt | 15.8 | 1 | 0 | [[Cepharanthine (drug)]] 5 µM 4.27× (z +9.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.0 | 1 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.81× (z +8.7) | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.144× (z -10.0) |
| [[RKO (line)]] | wt | 15.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0785× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 22.2 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.109× (z -8.5) |
| [[SW48 (line)]] | wt | 16.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0792× (z -9.3) |
| [[A-172 (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 35.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9473), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FDPS]] | +0.87 | +0.88 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 995 |
| [[ACSS2]] | +0.85 | +0.85 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 477 |
| [[SREBF2]] | +0.85 | +0.83 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 894 |
| [[FDFT1]] | +0.83 | +0.81 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 873 |
| [[SQLE]] | +0.83 | +0.80 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 906 |
| [[MSMO1]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | pathway: Cholesterol biosynthesis; STRING 752 |
| [[HMGCR]] | +0.79 | +0.77 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 896 |
| [[ERG28]] | +0.75 | +0.71 / +0.71 | both halves | 7e-06 | STRING 466 |
| [[DHCR7]] | +0.75 | +0.75 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 860 |
| [[EBP]] | +0.74 | +0.75 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_CHOLESTEROL_HOMEOSTASIS; STRING 668 |
| [[INSIG1]] | +0.73 | +0.75 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 492 |
| [[HSD17B7P2]] | +0.72 | +0.71 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF462]] | -0.57 | -0.47 / -0.58 | both halves | 2e-05 |  |
| [[TRMT5]] | -0.57 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[TFAM]] | -0.56 | -0.52 / -0.47 | both halves | 2e-05 |  |
| [[ENC1]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[CSTF2T]] | -0.54 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[MED1]] | -0.54 | -0.50 / -0.42 | both halves | 4e-05 | pathway: Activation of gene expression by SREBF (SREBP) |
| [[AASDHPPT]] | -0.54 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[ZNF507]] | -0.53 | -0.44 / -0.51 | both halves | 3e-05 |  |
| [[TBCEL]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[NSD1]] | -0.53 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[DDX20]] | -0.53 | -0.53 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB33]] | -0.53 | -0.39 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.855). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.5, -48.9); signed map (-53.2, 32.3). **Vector** length 135, 40.5% of its response variance represented; |z| ≥ 3 in 1,105 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.61 to 19); *Cholesterol biosynthesis via desmosterol (Bloch pathway)* (reactome, mean cos +0.66 to 8); *Zymostenol biosynthesis via lathosterol (Kandutsch-Russell pathway)* (reactome, mean cos +0.67 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cepharanthine (drug)]] 5 µM |  | +8.7 | +12.6 |
|  | [[Berbamine (drug)]] 5 µM |  | +7.3 | +12.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +8.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +6.8 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.1 | +6.2 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +4.5 | +4.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.5 | +1.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +4.5 | +4.6 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -9.4 | -5.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.1 | -6.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.6 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.4 | -6.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.3 | -5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.9 | -5.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.0 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | mevalonate diphosphate decarboxylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.2 — chr16:88,651,935-88,663,161 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MPD |
| Gene groups (HGNC) | Decarboxylases |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, APICAL_JUNCTION |
| Reactome | 10 pathways, smallest: Synthesis of dolichyl-phosphate; Lanosterol biosynthesis; Cholesterol biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [P53602](https://www.uniprot.org/uniprotkb/P53602) (Diphosphomevalonate decarboxylase):

> Catalyzes the ATP dependent decarboxylation of (R)-5-diphosphomevalonate to form isopentenyl diphosphate (IPP). Functions in the mevalonate (MVA) pathway leading to isopentenyl diphosphate (IPP), a key precursor for the biosynthesis of isoprenoids and sterol synthesis.

**Summary**, from NCBI Gene [4597](https://www.ncbi.nlm.nih.gov/gene/4597):

> The enzyme mevalonate pyrophosphate decarboxylase catalyzes the conversion of mevalonate pyrophosphate into isopentenyl pyrophosphate in one of the early steps in cholesterol biosynthesis. It decarboxylates and dehydrates its substrate while hydrolyzing ATP. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7529](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7529) · Entrez [4597](https://www.ncbi.nlm.nih.gov/gene/4597) · UniProt [P53602](https://www.uniprot.org/uniprotkb/P53602) · Ensembl [ENSG00000167508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000167508)

## Data

Gene col 9473: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9473); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9473, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9473]; `tensor/DDL_lfc|DDL_z.npy` [9473]; `embed/gene_vectors.npy` [9473]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9473 or target_col == 9473). Every well: [[MVD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MVD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
