---
symbol: "ATF5"
type: "gene"
col: 9760
ensembl_id: "ENSG00000169136"
name: "activating transcription factor 5"
location: "19q13.33"
module: 23
arm: "+"
pooled_cpm: 42.22
n_lines_expressing: 49
n_dd_up: 22
n_dd_down: 9
n_dd_up_clean: 15
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/023", "written"]
generated_by: "tahoemap"
---

# ATF5

*activating transcription factor 5* — 19q13.33

> [!summary] In one line
> ATF5 is a bZIP factor translated under the same eIF2-dependent control as [[ATF4]], best established as a brake on neural progenitor differentiation and as the mammalian mediator of a mitochondrial unfolded-protein response.

## What it is

Like [[ATF4]], ATF5 carries inhibitory upstream open reading frames and is translated preferentially when eIF2 is phosphorylated. Two functional accounts are reasonably supported. In the nervous system it keeps neural progenitors proliferating, must be downregulated for them to become neurons, and is needed for olfactory sensory neuron development. Separately, ATF5 can substitute for the worm factor ATFS-1 in mounting a mitochondrial unfolded-protein response — the leading mammalian candidate for that pathway. It is reported as pro-survival in glioma, on evidence from few laboratories. Overall ATF5 is substantially less characterised than its paralogue.

## What is uncertain

ATF5 and [[ATF4]] share translational control, dimerisation partners and a broadly similar consensus, so their inferred activities are expected to be collinear, and a signal credited to ATF5 may belong to the family. Its curated target set is small, which makes any activity inferred from it noisy. The mitochondrial-UPR role rests largely on cross-species complementation, and accounts of how ATF5 is held inactive — sequestration in mitochondria versus translational silence — are not reconciled.

## References

- Angelastro et al., 2003, Journal of Neuroscience — regulated ATF5 expression is required for neural progenitors to progress to neurons.
- Zhou et al., 2008, Journal of Biological Chemistry — eIF2 phosphorylation directs ATF5 translational control through its upstream open reading frames.
- Fiorese et al., 2016, Current Biology — ATF5 mediates a mammalian mitochondrial unfolded-protein response, rescuing atfs-1 loss in C. elegans.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.01× (z +19.0, q 0e+00, up in 42 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.363× (z -12.3, q 3e-32, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (79 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 21 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THAP2]] (+0.75, fdr 8e-05), [[PATL2]] (+0.74, fdr 5e-05), [[PPP1R12A-AS2]] (+0.73, fdr 5e-04); moves opposite to [[PCMT1]] (-0.66, fdr 1e-04), [[NHP2]] (-0.66, fdr 4e-04), [[LPCAT4]] (-0.65, fdr 2e-04).
> It sits in the **+** arm of [[Module 023]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9760.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.01×** | +19.0 | 0e+00 | 42/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +14.7 | 0e+00 | 41/46 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.90×** | +13.0 | 4e-36 | 37/46 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.62×** | +11.3 | 2e-27 | 38/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.59×** | +11.2 | 7e-27 | 36/42 (NCI-H2030, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.93×** | +7.7 | 1e-12 | 26/36 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.78×** | +7.0 | 2e-10 | 35/42 (J82, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.63×** | +6.0 | 2e-07 | 29/46 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.60×** | +5.7 | 6e-07 | 27/46 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.59×** | +5.7 | 7e-07 | 30/47 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +5.7 | 8e-07 | 23/41 (J82, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +5.0 | 2e-05 | 26/47 (SK-MEL-2, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +5.0 | 3e-05 | 26/47 (J82, HEC-1-A, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +4.9 | 4e-05 | 27/45 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[venetoclax (drug)]] 5 µM |  | **2.08×** | +4.7 | 1e-04 | 26/44 (H4, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.27×** | +4.1 | 0.001 | 22/47 (SW480, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.1 | 0.001 | 22/47 (LoVo, NCI-H460, …) | top dose only |  |
| [[Amsacrine (drug)]] 5 µM |  | 1.20× | +3.1 | 0.045 | 21/47 (J82, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.045 | 12/47 (NCI-H2030, LS 180, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9760.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.363×** | -12.3 | 3e-32 | 43/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.425×** | -10.4 | 5e-23 | 42/47 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.437×** | -10.1 | 1e-21 | 42/47 (PANC-1, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.473×** | -9.1 | 1e-17 | 41/45 (BT-474, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.479×** | -9.0 | 3e-17 | 42/47 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.373×** | -6.3 | 3e-08 | 35/47 (NCI-H2030, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.516×** | -4.2 | 0.002 | 22/47 (H4, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.796×** | -3.9 | 0.006 | 24/47 (A-172, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.559×** | -3.7 | 0.013 | 21/45 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 0.775× | -3.1 | 0.11 | 20/46 (AsPC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.770× | -3.0 | 0.14 | 16/46 (RKO, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9760. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 471 | 0 | 11 (6 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.275× (z -12.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -11.8) |
| [[PANC-1 (line)]] | alt | 62.1 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +19.6) | [[Belinostat (drug)]] 5 µM 0.226× (z -14.9) |
| [[HEC-1-A (line)]] | alt | 36.8 | 7 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.68× (z +16.7) | — |
| [[A498 (line)]] | wt | 37.0 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +17.0) | [[Panobinostat (drug)]] 0.5 µM 0.246× (z -12.2) |
| [[J82 (line)]] | alt | 19.7 | 6 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.52× (z +16.4) | — |
| [[LS 180 (line)]] | wt | 27.1 | 3 | 3 | [[Homoharringtonine (drug)]] 5 µM 5.08× (z +15.7) | [[Belinostat (drug)]] 5 µM 0.170× (z -12.1) |
| [[NCI-H2030 (line)]] | alt | 85.8 | 5 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +16.3) | [[Belinostat (drug)]] 5 µM 0.353× (z -9.1) |
| [[A-427 (line)]] | wt | 76.0 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.219× (z -12.9) |
| [[A549 (line)]] | wt | 27.2 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.87× (z +15.3) | — |
| [[HS-578T (line)]] | alt | 18.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.56× (z +14.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 98.1 | 3 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.58× (z +9.9) | [[Panobinostat (drug)]] 5 µM 0.254× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 14.3 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.44× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 54.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.01× (z +13.4) | — |
| [[A-172 (line)]] | wt | 45.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +11.7) | [[Belinostat (drug)]] 5 µM 0.313× (z -8.5) |
| [[BT-474 (line)]] | alt | 24.2 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.38× (z +10.3) | [[Belinostat (drug)]] 0.5 µM 0.136× (z -11.9) |
| [[C32 (line)]] | wt | 13.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.17× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 22.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +12.4) | — |
| [[LoVo (line)]] | wt | 22.7 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 34.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.241× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 14.8 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +11.2) | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +13.4) | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.81× (z +14.6) | — |
| [[Hs 766T (line)]] | wt | 13.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.88× (z +12.7) | — |
| [[SNU-1 (line)]] | wt | 57.7 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.129× (z -11.7) |
| [[C-33 A (line)]] | alt | 61.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.193× (z -10.5) |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.141× (z -9.2) |
| [[H4 (line)]] | wt | 74.1 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.146× (z -10.5) |
| [[HCT15 (line)]] | alt | 31.6 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.217× (z -8.7) |
| [[hTERT-HPNE (line)]] | wt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 41.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +11.0) | — |
| [[RKO (line)]] | wt | 20.4 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.161× (z -10.4) |
| [[SK-MEL-2 (line)]] | alt | 19.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.34× (z +9.8) | — |
| [[SNU-423 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.98× (z +11.2) | — |
| [[SW 900 (line)]] | alt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +9.4) | — |
| [[SW48 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.202× (z -8.5) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +14.7) | — |
| [[AN3 CA (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.09 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9760), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 21 of them with an alert (⚠; 21 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THAP2]] | +0.75 | +0.73 / +0.37 | both halves | 8e-05 |  |
| [[PATL2]] | +0.74 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.73 / +0.23 | both halves | 5e-04 |  |
| [[OXA1L-DT]] | +0.73 | +0.74 / +0.28 | both halves | 3e-04 |  |
| [[ATE1OSP]] | +0.72 | +0.71 / +0.32 | both halves | 2e-04 |  |
| [[PBDC1]] | +0.72 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[LINC01004]] | +0.71 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[LINC00571]] | +0.71 | +0.64 / +0.37 | both halves | 8e-05 |  |
| [[BRPF3]] | +0.70 | +0.70 / +0.37 | both halves | 7e-05 |  |
| [[GABPB2]] | +0.70 | +0.74 / +0.33 | both halves | 1e-04 |  |
| [[KRBOX5]] | +0.70 | +0.69 / +0.38 | both halves | 6e-05 |  |
| [[SLFN5]] | +0.70 | +0.73 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCMT1]] | -0.66 | -0.61 / -0.33 | both halves | 1e-04 |  |
| [[NHP2]] | -0.66 | -0.56 / -0.25 | both halves | 4e-04 |  |
| [[LPCAT4]] | -0.65 | -0.65 / -0.32 | both halves | 2e-04 |  |
| [[LRFN3]] | -0.65 | -0.57 / -0.31 | both halves | 2e-04 |  |
| [[METAP1]] | -0.64 | -0.63 / -0.47 | both halves | 2e-05 | same gene group |
| [[WASF3]] | -0.64 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[ATRN]] | -0.62 | -0.61 / -0.26 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ATF5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LINC00944]] | B | LINC00944 activity lowers ATF5's level | lines that do not express LINC00944 (20) vs lines expressing it (30) | 1.58× higher at baseline in the lines without LINC00944 | 0.043 | ⚠ within organs, on part of the lines; also absent: RDUR, ENSG00000289600, LINC02405 |
| [[ZNF785]] | B | ZNF785 activity lowers ATF5's level | lines that do not express ZNF785 (9) vs lines expressing it (41) | 1.68× higher at baseline in the lines without ZNF785 | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFRSF14, BDH1, PARP8 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ATF5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ATF5's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC02100]] | B | LINC02100 activity lowers ATF5's level | lines that do not express LINC02100 (9) vs lines expressing it (41) | 1.87× higher at baseline in the lines without LINC02100 | 0.089 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, RASA3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.752). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (5.4, 11.7); signed map (21.5, -11.3). **Vector** length 119, 34.7% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +9.8 | +19.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.2 | +11.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +13.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.5 | +11.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.8 | +5.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.1 | +1.2 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | +3.1 | +2.4 |
| fall | [[Belinostat (drug)]] 5 µM |  | -8.8 | -12.3 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -8.8 | -9.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -8.3 | -9.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -7.1 | -10.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -7.0 | -10.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -5.2 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.6 | -3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -3.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -2.2 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.7 | +1.1 |

## What is on record

|  |  |
|---|---|
| Name | activating transcription factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:49,928,702-49,933,935 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Activating transcription factor 4 family |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, G2M_CHECKPOINT |
| Reactome | 4 pathways, smallest: Response of EIF2AK1 (HRI) to heme deficiency; Mitochondrial unfolded protein response (UPRmt); Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y2D1](https://www.uniprot.org/uniprotkb/Q9Y2D1) (Cyclic AMP-dependent transcription factor ATF-5):

> Transcription factor that either stimulates or represses gene transcription through binding of different DNA regulatory elements such as cAMP response element (CRE) (consensus: 5'-GTGACGT[AC][AG]-3'), ATF5-specific response element (ARE) (consensus: 5'-C[CT]TCT[CT]CCTT[AT]-3') but also the amino acid response element (AARE), present in many viral and cellular promoters. Critically involved, often in a cell type-dependent manner, in cell survival, proliferation, and differentiation. Its …

**Summary**, from NCBI Gene [22809](https://www.ncbi.nlm.nih.gov/gene/22809):

> Enables several functions, including DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II transcription regulatory region sequence-specific DNA binding activity; and tubulin binding activity. Involved in several processes, including fat cell differentiation; regulation of DNA-templated transcription; and regulation of cell cycle process. Located in centrosome; cytosol; and nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:790](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:790) · Entrez [22809](https://www.ncbi.nlm.nih.gov/gene/22809) · UniProt [Q9Y2D1](https://www.uniprot.org/uniprotkb/Q9Y2D1) · Ensembl [ENSG00000169136](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169136)

## Data

Gene col 9760: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9760); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9760, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9760]; `tensor/DDL_lfc|DDL_z.npy` [9760]; `embed/gene_vectors.npy` [9760]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9760 or target_col == 9760). Every well: [[ATF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/ATF5.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
